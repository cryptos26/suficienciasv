import unittest
import uuid
from app import app
import database as db

class TestMonetizationAndLicensing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import shutil, tempfile, os
        cls.orig_db = db.DB_PATH
        cls.tmp_dir = tempfile.mkdtemp()
        cls.tmp_db = os.path.join(cls.tmp_dir, "test_notariado.db")
        shutil.copyfile(cls.orig_db, cls.tmp_db)
        db.DB_PATH = cls.tmp_db

    @classmethod
    def tearDownClass(cls):
        import shutil, os
        db.DB_PATH = cls.orig_db
        if os.path.exists(cls.tmp_db):
            try: os.remove(cls.tmp_db)
            except Exception: pass
        if os.path.exists(cls.tmp_dir):
            try: shutil.rmtree(cls.tmp_dir, ignore_errors=True)
            except Exception: pass

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_single_device_restriction(self):
        dev1 = f"device_pc_{uuid.uuid4().hex[:6]}"
        dev2 = f"device_pc_{uuid.uuid4().hex[:6]}"

        # Generate a test license
        lic = db.admin_create_license(plan_type="vitalicia", duration_days=-1, notes="Test Single Device")
        key = lic["key"]

        # Device 1 activates key
        res1 = db.validate_or_activate_license(key, dev1)
        self.assertTrue(res1["success"], "Device 1 should successfully activate")

        # Device 2 tries to activate the same key
        res2 = db.validate_or_activate_license(key, dev2)
        self.assertFalse(res2["success"], "Device 2 must be REJECTED (single device lock)")
        self.assertTrue(res2.get("is_locked_other_device"), "Should flag that key is locked to other device")

        # Device 1 accesses again
        res3 = db.validate_or_activate_license(key, dev1)
        self.assertTrue(res3["success"], "Device 1 must be accepted again on subsequent checks")

    def test_automated_checkout_option_1(self):
        dev = f"laptop_carlos_{uuid.uuid4().hex[:6]}"
        # Test automated online purchase
        res = self.client.post("/api/checkout/process", json={
            "plan_type": "vitalicia",
            "buyer_name": "Lic. Carlos Alvarado",
            "buyer_email": "carlos@abogados.sv",
            "buyer_phone": "7888-9999",
            "device_id": dev
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data["success"])
        self.assertTrue(data["license_key"].startswith("NOT-VITA-"))
        self.assertEqual(data["amount_usd"], 34.99)

        # Verify device is now licensed
        lic = db.check_device_license(dev)
        self.assertIsNotNone(lic)
        self.assertEqual(lic["license_key"], data["license_key"])

    def test_disclaimer_page(self):
        res = self.client.get("/terminos")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Descargo Integral de Responsabilidad", res.data)
        self.assertIn(b"Corte Suprema de Justicia", res.data)
        self.assertIn(b"San Salvador", res.data)

    def test_promotional_keys_seeded(self):
        keys = db.get_promotional_keys()
        self.assertGreaterEqual(len(keys), 10)
        self.assertTrue(all(k["plan_type"] == "vitalicia" for k in keys))

    def test_multi_gateway_payment_processing(self):
        gateways = [
            ("strike", "STRIKE-TX-98765"),
            ("blink", "BLINK-INV-54321"),
            ("banco", "REF-BANCO-AGRICOLA-001"),
            ("nequi", "NEQUI-TRF-112233")
        ]
        for method, ref in gateways:
            dev = f"dev_gw_{method}_{uuid.uuid4().hex[:4]}"
            res = self.client.post("/api/checkout/process", json={
                "plan_type": "30_dias",
                "buyer_name": f"Aspirante {method.capitalize()}",
                "buyer_email": f"aspirante_{method}@correo.sv",
                "buyer_phone": "7111-2222",
                "payment_method": method,
                "payment_reference": ref,
                "device_id": dev
            })
            self.assertEqual(res.status_code, 200)
            data = res.get_json()
            self.assertTrue(data["success"])
            self.assertEqual(data["payment_method"], method)
            self.assertEqual(data["payment_reference"], ref)
            self.assertIn("whatsapp_url", data)
            self.assertIn("https://wa.me/", data["whatsapp_url"])

            # Verify order in DB
            orders = db.admin_get_orders()
            matching = [o for o in orders if o["order_id"] == data["order_id"]]
            self.assertTrue(len(matching) > 0)
            self.assertEqual(matching[0]["payment_method"], method)
            self.assertEqual(matching[0]["payment_reference"], ref)

    def test_vercel_entrypoint_import(self):
        """Verifies that api/index.py can be loaded by Vercel serverless runtime without error."""
        import api.index as vercel_app
        self.assertIsNotNone(vercel_app.app)

    def test_ambassador_referral_and_strike_commission(self):
        # 1. Test validate existing ambassador
        res_val = self.client.get("/api/referral/validate?code=SUFICIENCIA-VIP&plan=vitalicia")
        self.assertEqual(res_val.status_code, 200)
        data_val = res_val.get_json()
        self.assertTrue(data_val["valid"])
        self.assertEqual(data_val["discount"], 5.0)
        self.assertEqual(data_val["discounted_price"], 29.99)

        # 2. Test validate non-existent ambassador
        res_fake = self.client.get("/api/referral/validate?code=CODIGO-FALSO-999&plan=vitalicia")
        self.assertEqual(res_fake.status_code, 404)
        self.assertFalse(res_fake.get_json()["valid"])

        # 3. Process checkout with referral code
        dev = f"dev_ref_{uuid.uuid4().hex[:6]}"
        res_checkout = self.client.post("/api/checkout/process", json={
            "plan_type": "vitalicia",
            "buyer_name": "Lic. Referido Por Colega",
            "buyer_email": "referido@abogado.sv",
            "buyer_phone": "7999-8888",
            "payment_method": "strike",
            "payment_reference": "STRIKE-DISCOUNT-01",
            "referral_code": "SUFICIENCIA-VIP",
            "device_id": dev
        })
        self.assertEqual(res_checkout.status_code, 200)
        order_data = res_checkout.get_json()
        self.assertTrue(order_data["success"])
        self.assertEqual(order_data["amount_usd"], 29.99)
        self.assertEqual(order_data["discount_usd"], 5.0)
        self.assertEqual(order_data["referral_code"], "SUFICIENCIA-VIP")

        # 4. Verify Commission recorded in database for Strike payout
        commissions = db.get_commissions(status="PENDIENTE")
        matching_comm = [c for c in commissions if c["order_id"] == order_data["order_id"]]
        self.assertEqual(len(matching_comm), 1, "Must record exactly 1 commission for the order")
        comm = matching_comm[0]
        self.assertEqual(comm["amount_usd"], 5.0, "Vitalicia plan gives $5.00 USD commission")
        self.assertEqual(comm["strike_handle"], "miltonrb")
        self.assertEqual(comm["status"], "PENDIENTE")

        # 5. Mark commission as paid via Strike
        comm_id = comm.get("comm_id") or comm.get("id")
        db.mark_commission_paid(comm_id, payout_reference="TX-STRIKE-PAID-001")
        paid_comms = db.get_commissions(status="PAGADO")
        matching_paid = [c for c in paid_comms if (c.get("comm_id") == comm_id or c.get("id") == comm_id)]
        self.assertEqual(len(matching_paid), 1)
        self.assertEqual(matching_paid[0]["status"], "PAGADO")

    def test_ambassador_public_registration(self):
        new_code = f"AMB-{uuid.uuid4().hex[:4].upper()}"
        res = self.client.post("/api/ambassadors/register", json={
            "name": "Lic. Mario Zelaya",
            "email": "mario@notario.sv",
            "strike_handle": "marioz_strike",
            "code": new_code
        })
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.get_json()["success"])

        # Check ambassador exists
        amb = db.get_ambassador(new_code)
        self.assertIsNotNone(amb)
        self.assertEqual(amb["name"], "Lic. Mario Zelaya")
        self.assertEqual(amb["strike_handle"], "marioz_strike")

if __name__ == "__main__":
    unittest.main()
