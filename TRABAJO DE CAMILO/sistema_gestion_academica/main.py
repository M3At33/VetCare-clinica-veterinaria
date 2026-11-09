"""
Sistema de Gestión Académica
Archivo principal para ejecutar y probar el sistema.
"""

from modelos.programa_academico import ProgramaAcademico
from modelos.asignatura import Asignatura
from modelos.estudiante import Estudiante
from modelos.docente import Docente
from modelos.administrativo import Administrativo


def ejecutar_pruebas_validaciones(programa, asignatura, estudiante):
    """Demuestra modificaciones válidas e intentos de modificación inválidos."""
    print("\n" + "=" * 65)
    print("PRUEBAS DE ENCAPSULAMIENTO Y VALIDACIONES")
    print("=" * 65)

    print("\n1. Modificación válida del correo de un estudiante:")
    estudiante.set_correo("laura.actualizada@universidad.edu.co")
    print("Correo actualizado:", estudiante.get_correo())

    print("\n2. Intento de asignar un correo vacío:")
    try:
        estudiante.set_correo("   ")
    except ValueError as error:
        print("Validación correcta:", error)

    print("\n3. Intento de asignar cero semestres al programa:")
    try:
        programa.set_numero_semestres(0)
    except ValueError as error:
        print("Validación correcta:", error)

    print("\n4. Intento de asignar créditos negativos a la asignatura:")
    try:
        asignatura.set_creditos(-2)
    except ValueError as error:
        print("Validación correcta:", error)

    print("\n5. Intento de asignar un promedio fuera del rango permitido:")
    try:
        estudiante.set_promedio_acumulado(6.5)
    except ValueError as error:
        print("Validación correcta:", error)


def main():
    print("=" * 65)
    print("SISTEMA DE GESTIÓN ACADÉMICA")
    print("=" * 65)

    # Fase 1: creación de programas académicos y asignaturas.
    trabajo_social = ProgramaAcademico(
        "TS001", "Trabajo Social", "Facultad de Ciencias Sociales", 10
    )
    ingenieria_sistemas = ProgramaAcademico(
        "IS001", "Ingeniería de Sistemas", "Facultad de Ingeniería", 10
    )

    asignatura_poo = Asignatura(
        "POO101", "Programación Orientada a Objetos", 3, ingenieria_sistemas
    )
    asignatura_intervencion = Asignatura(
        "TS203", "Metodología de Intervención Social", 4, trabajo_social
    )

    print("\nPROGRAMAS ACADÉMICOS")
    trabajo_social.mostrar_informacion()
    ingenieria_sistemas.mostrar_informacion()

    print("\nASIGNATURAS")
    asignatura_poo.mostrar_informacion()
    asignatura_intervencion.mostrar_informacion()

    # Fases 3 y 4: objetos de las clases derivadas.
    estudiante1 = Estudiante(
        "1001", "Laura Gómez", "laura@universidad.edu.co",
        "EST001", trabajo_social, 6, 4.2
    )
    estudiante2 = Estudiante(
        "1002", "Andrés Pérez", "andres@universidad.edu.co",
        "EST002", ingenieria_sistemas, 4, 3.8
    )

    docente1 = Docente(
        "2001", "María Rodríguez", "maria@universidad.edu.co",
        "DOC001", "Facultad de Ciencias Sociales", "Tiempo completo", 40
    )
    docente2 = Docente(
        "2002", "Carlos Torres", "carlos@universidad.edu.co",
        "DOC002", "Facultad de Ingeniería", "Cátedra", 12
    )

    administrativo1 = Administrativo(
        "3001", "Diana Martínez", "diana@universidad.edu.co",
        "ADM001", "Registro Académico", "Coordinadora", "Tiempo completo"
    )
    administrativo2 = Administrativo(
        "3002", "Julián Castro", "julian@universidad.edu.co",
        "ADM002", "Bienestar Universitario", "Auxiliar administrativo", "Medio tiempo"
    )

    ejecutar_pruebas_validaciones(trabajo_social, asignatura_poo, estudiante1)

    # Fase 5: una colección heterogénea y un solo ciclo polimórfico.
    personas = [
        estudiante1, estudiante2,
        docente1, docente2,
        administrativo1, administrativo2
    ]

    print("\n" + "=" * 65)
    print("REPORTE POLIMÓRFICO DE PERSONAS")
    print("=" * 65)

    for persona in personas:
        persona.mostrar_informacion()
        persona.realizar_actividad_principal()
        print("-" * 65)


if __name__ == "__main__":
    main()
