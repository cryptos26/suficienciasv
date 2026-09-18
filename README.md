# Sistema de Estudio y Simulación del Examen de Notariado de El Salvador (CSJ)

Plataforma interactiva diseñada específicamente para abogados salvadoreños aspirantes a la función notarial. Diseñada para simular con el más alto grado de fidelidad las condiciones del **Examen de Suficiencia para el Ejercicio de la Función Notarial** administrado anualmente por la **Corte Suprema de Justicia (CSJ)**.

---

## 🏛️ Características Principales

1. **Simulador Oficial de Examen CSJ**:
   - **Formato Oficial**: 20 preguntas seleccionadas al azar con distribución ponderada por ramas del derecho.
   - **Cronómetro Estricto**: 25 minutos con alertas visuales de tiempo por agotarse (< 5 min en amarillo, < 2 min en rojo pulsante).
   - **Herramienta de Duda / Bandera**: Marca preguntas para revisarlas antes de entregar.
   - **Escala de Calificación Oficial**: 0.0 a 10.0 (Aprobado con nota igual o mayor a 7.0).
   - **Seguridad Antifraude**: Las respuestas correctas y justificaciones no se transmiten al navegador durante la prueba activa para evitar consultas en el inspector de elementos.

2. **Justificación Jurídica Exhaustiva**:
   - **Cita Exacta de la Ley y Artículo**: *Ley de Notariado (LN), LENJVOD, Código Civil (C.C.), Código de Familia (C.F.), CPCM, Código de Comercio (C.Com.) y Leyes Registrales (CNR)*.
   - **Fundamentación del Caso Práctico**: Análisis de la doctrina y técnica notarial salvadoreña.
   - **Desglose de Distractores / Trampas de la CSJ**: Demostración punto por punto de por qué las opciones alternativas son incorrectas (confusión entre nulidad instrumental vs nulidad de la obligación, plazos de sede judicial vs notarial, etc.).

3. **Modalidad de Práctica Guiada por Materias**:
   - Selección por rama jurídica:
     - *Ley de Notariado y Función Notarial*
     - *Jurisdicción Voluntaria Notarial (LENJVOD)*
     - *Derecho Civil y Régimen Sucesorio*
     - *Derecho de Familia y Menores*
     - *Derecho Mercantil y Títulos Valores*
     - *Derecho Registral y Catastro (CNR)*
   - Retroalimentación inmediata con un clic en **"Comprobar Respuesta"**.

4. **Fichas Mnemotécnicas 3D (Flashcards)**:
   - Tarjetas interactivas para memorizar plazos perentorios fatales y requisitos de testigos instrumentales (3 testigos en testamento abierto, 5 en testamento cerrado, 15 días para entregar libro de protocolo, 15 días para remitir testimonio de matrimonio, etc.).
   - Volteo 3D mediante clic o tecla `Espacio`.

5. **Perfil de Usuario y Cuenta Regresiva CSJ (`/perfil`)**:
   - Identificación del aspirante (Nombre, Alma Mater / Universidad de egreso, Carné/Acuerdo CSJ de Abogado).
   - **Contador regresivo inteligente**: Muestra los días restantes exactos para la fecha meta proyectada de la convocatoria de la CSJ.
   - Diagnóstico personal de rendimiento acumulado (Promedio, porcentaje de aprobación, número de simulacros).
   - Estado de seguridad del dispositivo vinculado (`device_id`) y plan de licencia activo.
   - Formulario de edición con guardado asíncrono e instantáneo en la base de datos.

6. **Panel y Registro Histórico**:
   - Seguimiento de calificaciones por intento, tiempo promedio empleado y desglose de debilidades y fortalezas por materia.

## 💳 Sistema de Monetización, Licencias y Seguridad

Se ha implementado el modelo de **Automatización Total (Opción 1)** y control de acceso:

1. **Restricción a un Solo Dispositivo (Single-Device Lock)**:
   - Cada clave de licencia queda vinculada criptográficamente a la computadora/navegador del usuario al momento de activarse.
   - Si otra persona intenta ingresar la misma clave en un dispositivo diferente, el sistema bloquea el acceso informando que la licencia es personal e intransferible.
   - El propietario cuenta con una herramienta en el Panel Admin para "Liberar Dispositivo" si un cliente legítimamente renueva su equipo.

2. **Compra en Línea y Entrega 100% Automatizada (`/comprar`)**:
   - Formulario de checkout con selección de planes (30 días $19.99, 90 días $34.99, Vitalicia $49.99).
   - Generación instantánea de clave y desbloqueo automático del equipo en el mismo milisegundo.
   - Endpoint para webhooks de pasarelas salvadoreñas (Wompi / Banco Agrícola).

3. **Aviso Legal y Descargo de Responsabilidad (Disclaimer) (`/terminos`)**:
   - Texto jurídico formal visible en el pie de página de toda la aplicación y en el flujo de activación.
   - Aclara el carácter académico independiente (sin patrocinio oficial de la CSJ), la ausencia de garantía de aprobación en la prueba real, el licenciamiento personal para un solo equipo y los derechos de autor.

4. **10 Claves Promocionales Vitalicias Generadas**:
   - Registradas en la base de datos para entrega inmediata a los primeros 10 aspirantes VIP.

5. **Panel de Administración Privado (`/admin`)**:
   - Protegido por PIN (`notario2026`).
   - Permite copiar mensajes listos para WhatsApp, generar nuevas claves en 1 clic o en lotes, y gestionar el inventario de ventas.

---

## 🚀 Instrucciones de Uso

El proyecto se encuentra ubicado en:
`C:\Users\MINEDUCYT\Desktop\antigravity\simulador_notariado_sv`

Para iniciar el sistema tienes dos accesos directos listos:
1. **Acceso directo en la carpeta principal**:
   Haz doble clic en [`Iniciar_Simulador_Notariado.bat`](file:///C:/Users/MINEDUCYT/Desktop/antigravity/Iniciar_Simulador_Notariado.bat) ubicado en `C:\Users\MINEDUCYT\Desktop\antigravity\`.
2. **O dentro de la carpeta del proyecto**:
   Ejecuta [`iniciar_simulador.bat`](file:///C:/Users/MINEDUCYT/Desktop/antigravity/simulador_notariado_sv/iniciar_simulador.bat) o por PowerShell:
   ```powershell
   cd C:\Users\MINEDUCYT\Desktop\antigravity\simulador_notariado_sv
   python app.py
   ```
3. El sistema se abrirá automáticamente en tu navegador web en: **`http://127.0.0.1:5000`**

---

## 📂 Estructura del Proyecto

```
simulador_notariado_sv/
├── app.py                     # Servidor web Flask y rutas API
├── database.py                # Gestión de base de datos SQLite y persistencia
├── questions_seed.py          # Banco de casos prácticos fundamentados y flashcards
├── test_app.py                # Suite de pruebas unitarias y de integración
├── iniciar_simulador.bat      # Lanzador de un solo clic para Windows
├── notariado.db               # Base de datos SQLite (se genera automáticamente)
├── static/
│   ├── css/
│   │   └── custom.css         # Tipografías jurídicas, estilos 3D y cronómetro
│   └── js/
│       ├── exam.js            # Lógica del simulador CSJ cronometrado
│       ├── practice.js        # Lógica de la práctica por materias
│       └── flashcards.js      # Lógica de las fichas mnemotécnicas
└── templates/
    ├── base.html              # Plantilla institucional con navegación responsiva
    ├── index.html             # Dashboard principal con estadísticas
    ├── exam.html              # Pantalla oficial de examen
    ├── results.html           # Dictamen final y justificaciones desglosadas
    ├── practice.html          # Modo estudio guiado con feedback instantáneo
    ├── flashcards.html        # Fichas 3D de plazos
    └── history.html           # Historial y registro de calificaciones
```
