"""Clase que representa un programa académico."""


class ProgramaAcademico:
    def __init__(self, codigo, nombre, facultad, numero_semestres):
        self.__codigo = self._validar_texto(codigo, "El código")
        self.__nombre = self._validar_texto(nombre, "El nombre")
        self.__facultad = self._validar_texto(facultad, "La facultad")
        self.__numero_semestres = self._validar_semestres(numero_semestres)

    @staticmethod
    def _validar_texto(valor, campo):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"{campo} no puede estar vacío.")
        return valor.strip()

    @staticmethod
    def _validar_semestres(numero):
        if not isinstance(numero, int) or isinstance(numero, bool) or numero <= 0:
            raise ValueError("El número de semestres debe ser un entero mayor que cero.")
        return numero

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = self._validar_texto(codigo, "El código")

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = self._validar_texto(nombre, "El nombre")

    def get_facultad(self):
        return self.__facultad

    def set_facultad(self, facultad):
        self.__facultad = self._validar_texto(facultad, "La facultad")

    def get_numero_semestres(self):
        return self.__numero_semestres

    def set_numero_semestres(self, numero):
        self.__numero_semestres = self._validar_semestres(numero)

    def mostrar_informacion(self):
        print(f"Código: {self.__codigo}")
        print(f"Nombre del programa: {self.__nombre}")
        print(f"Facultad: {self.__facultad}")
        print(f"Número de semestres: {self.__numero_semestres}")
