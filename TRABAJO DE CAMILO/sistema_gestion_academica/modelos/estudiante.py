"""Clase Estudiante: hereda los datos comunes de Persona."""


from modelos.persona import Persona


class Estudiante(Persona):
    def __init__(self, identificacion, nombre, correo, codigo_estudiantil,
                 programa_academico, semestre, promedio_acumulado):
        super().__init__(identificacion, nombre, correo)
        self.__codigo_estudiantil = self._validar_texto(codigo_estudiantil, "El código estudiantil")
        if programa_academico is None or not hasattr(programa_academico, "get_nombre"):
            raise ValueError("El estudiante debe tener un programa académico válido.")
        self.__programa_academico = programa_academico
        self.__semestre = self._validar_semestre(semestre)
        self.__promedio_acumulado = self._validar_promedio(promedio_acumulado)

    @staticmethod
    def _validar_texto(valor, campo):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"{campo} no puede estar vacío.")
        return valor.strip()

    @staticmethod
    def _validar_semestre(semestre):
        if not isinstance(semestre, int) or isinstance(semestre, bool) or semestre <= 0:
            raise ValueError("El semestre debe ser un entero mayor que cero.")
        return semestre

    @staticmethod
    def _validar_promedio(promedio):
        if not isinstance(promedio, (int, float)) or isinstance(promedio, bool) or not 0 <= promedio <= 5:
            raise ValueError("El promedio acumulado debe estar entre 0.0 y 5.0.")
        return float(promedio)

    def get_codigo_estudiantil(self):
        return self.__codigo_estudiantil

    def set_codigo_estudiantil(self, codigo):
        self.__codigo_estudiantil = self._validar_texto(codigo, "El código estudiantil")

    def get_programa_academico(self):
        return self.__programa_academico

    def set_programa_academico(self, programa):
        if programa is None or not hasattr(programa, "get_nombre"):
            raise ValueError("Debe seleccionar un programa académico válido.")
        self.__programa_academico = programa

    def get_semestre(self):
        return self.__semestre

    def set_semestre(self, semestre):
        self.__semestre = self._validar_semestre(semestre)

    def get_promedio_acumulado(self):
        return self.__promedio_acumulado

    def set_promedio_acumulado(self, promedio):
        self.__promedio_acumulado = self._validar_promedio(promedio)

    def mostrar_informacion(self):
        print("\nTIPO: ESTUDIANTE")
        super().mostrar_informacion()
        print(f"Código estudiantil: {self.__codigo_estudiantil}")
        print(f"Programa académico: {self.__programa_academico.get_nombre()}")
        print(f"Semestre: {self.__semestre}")
        print(f"Promedio acumulado: {self.__promedio_acumulado:.2f}")

    def realizar_actividad_principal(self):
        print(
            f"Actividad principal: cursa {self.__programa_academico.get_nombre()} "
            f"y está en el semestre {self.__semestre}."
        )
