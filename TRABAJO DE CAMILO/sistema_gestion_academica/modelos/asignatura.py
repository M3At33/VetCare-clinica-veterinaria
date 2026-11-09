"""Clase que representa una asignatura asociada a un programa académico."""


class Asignatura:
    def __init__(self, codigo, nombre, creditos, programa_academico):
        self.__codigo = self._validar_texto(codigo, "El código")
        self.__nombre = self._validar_texto(nombre, "El nombre")
        self.__creditos = self._validar_creditos(creditos)
        if programa_academico is None or not hasattr(programa_academico, "get_nombre"):
            raise ValueError("La asignatura debe estar asociada a un programa académico.")
        self.__programa_academico = programa_academico

    @staticmethod
    def _validar_texto(valor, campo):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"{campo} no puede estar vacío.")
        return valor.strip()

    @staticmethod
    def _validar_creditos(creditos):
        if not isinstance(creditos, int) or isinstance(creditos, bool) or creditos <= 0:
            raise ValueError("El número de créditos debe ser un entero mayor que cero.")
        return creditos

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = self._validar_texto(codigo, "El código")

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = self._validar_texto(nombre, "El nombre")

    def get_creditos(self):
        return self.__creditos

    def set_creditos(self, creditos):
        self.__creditos = self._validar_creditos(creditos)

    def get_programa_academico(self):
        return self.__programa_academico

    def set_programa_academico(self, programa_academico):
        if programa_academico is None or not hasattr(programa_academico, "get_nombre"):
            raise ValueError("Debe seleccionar un programa académico válido.")
        self.__programa_academico = programa_academico

    def mostrar_informacion(self):
        print(f"Código: {self.__codigo}")
        print(f"Nombre de la asignatura: {self.__nombre}")
        print(f"Número de créditos: {self.__creditos}")
        print(f"Programa académico: {self.__programa_academico.get_nombre()}")
