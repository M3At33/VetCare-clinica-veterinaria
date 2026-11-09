# Sistema de Gestión Académica

## Integrantes
- Integrante 1: [CAMILO ARIAS ARIAS]
- Integrante 2: [Escribir nombre completo]
- Integrante 3: [Escribir nombre completo]
- Integrante 4: [Escribir nombre completo]
- Integrante 5: [Escribir nombre completo]

> El equipo debe borrar las líneas de integrantes que no correspondan y completar los nombres reales.

## Descripción general
Proyecto académico desarrollado en Python para representar información básica de una comunidad universitaria. El sistema permite crear programas académicos, asignaturas, estudiantes, docentes y administrativos; consultar información; modificar atributos de forma controlada y mostrar las actividades principales de cada tipo de persona.

## Requisitos
- Python 3.10 o superior recomendado.
- No requiere instalar librerías externas.

## Estructura de archivos
```text
sistema_gestion_academica/
├── main.py
├── README.md
└── modelos/
    ├── __init__.py
    ├── persona.py
    ├── programa_academico.py
    ├── asignatura.py
    ├── estudiante.py
    ├── docente.py
    └── administrativo.py
```

## Cómo ejecutar
1. Descargue o clone el repositorio.
2. Abra la carpeta del proyecto en Visual Studio Code.
3. Abra una terminal dentro de esa carpeta.
4. Ejecute:
   ```bash
   python main.py
   ```
   Si el comando anterior no funciona en Windows, pruebe:
   ```bash
   py main.py
   ```

## Conceptos de programación orientada a objetos
- **Clases y objetos:** las clases definen la información y los comportamientos; el programa principal crea objetos de cada clase.
- **Constructores:** `__init__()` inicializa los atributos al crear cada objeto.
- **Encapsulamiento:** los atributos se definen como privados usando doble guion bajo (`__`). Se consultan y modifican mediante métodos.
- **Validaciones:** los métodos de modificación rechazan valores no permitidos y muestran el error correspondiente.
- **Herencia:** `Estudiante`, `Docente` y `Administrativo` heredan de `Persona`, reutilizando identificación, nombre y correo.
- **Sobreescritura:** las tres clases derivadas redefinen `mostrar_informacion()` y `realizar_actividad_principal()` para adaptar el comportamiento.
- **Polimorfismo:** una sola lista contiene objetos de las tres clases derivadas. Un único ciclo llama los mismos métodos y Python ejecuta la versión correspondiente al objeto, sin condicionales por tipo.

## Pruebas demostradas
- Creación de dos programas académicos y dos asignaturas.
- Creación de seis personas: dos estudiantes, dos docentes y dos administrativos.
- Consulta de la información de los objetos.
- Modificación válida del correo de un estudiante.
- Intentos de asignar correo vacío, cero semestres, créditos negativos y promedio fuera de rango.
- Presentación de actividades particulares mediante polimorfismo.

## Uso de herramientas de inteligencia artificial
Se utilizó ChatGPT como apoyo para organizar una propuesta inicial de estructura, generar y revisar fragmentos de código y explicar conceptos de programación orientada a objetos. Los integrantes del equipo deben revisar, probar, comprender y adaptar el proyecto, y poder explicar las decisiones tomadas durante su desarrollo.


