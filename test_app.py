import unittest
from app import app
import database as db

class TestNotariadoSimulador(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_dashboard_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Examen de Suficiencia Notarial CSJ', response.data)

    def test_simulador_route(self):
        response = self.client.get('/simulador')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Navegador de Preguntas', response.data)

    def test_exam_generate_api(self):
        response = self.client.get('/api/exam/generate')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertGreater(len(data['questions']), 0)
        # Ensure correct answers and justifications are NOT exposed in generate API
        for q in data['questions']:
            self.assertNotIn('correct_option', q)
            self.assertNotIn('justification', q)

    def test_exam_submit_and_evaluation(self):
        # Fetch questions first
        conn = db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, correct_option FROM questions LIMIT 5")
        rows = cursor.fetchall()
        conn.close()

        answers = {str(r['id']): r['correct_option'] for r in rows}

        response = self.client.post('/api/exam/submit', json={
            'time_spent_seconds': 600,
            'answers': answers
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['score'], 10.0) # all 5 are correct
        self.assertTrue(data['passed'])
        self.assertIn('/resultado/', data['redirect_url'])

    def test_practice_api(self):
        response = self.client.get('/api/practice/questions?category=notariado_puro')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertGreater(len(data['questions']), 0)
        # Practice mode DOES include justification
        self.assertIn('justification', data['questions'][0])
        self.assertIn('legal_basis', data['questions'][0])

    def test_flashcards_api(self):
        response = self.client.get('/api/flashcards?category=all')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertGreater(len(data['flashcards']), 0)

    def test_history_route(self):
        response = self.client.get('/historial')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Historial de Simulacros Realizados', response.data)

    def test_profile_route(self):
        response = self.client.get('/perfil')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Mi Perfil de Aspirante', response.data)

    def test_profile_update_api(self):
        response = self.client.post('/api/profile/update', json={
            'device_id': 'test_profile_dev_1',
            'full_name': 'Lic. Ana Sofía Martínez',
            'university': 'Universidad Dr. José Matías Delgado',
            'lawyer_id': '19450',
            'target_exam_date': '2026-11-28',
            'email': 'ana.sofia@derecho.sv',
            'phone': '7999-1122'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])

        # Verify saved in DB
        prof = db.get_user_profile('test_profile_dev_1')
        self.assertEqual(prof['full_name'], 'Lic. Ana Sofía Martínez')
        self.assertEqual(prof['university'], 'Universidad Dr. José Matías Delgado')

if __name__ == '__main__':
    unittest.main()
