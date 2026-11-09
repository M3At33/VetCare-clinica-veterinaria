"""Clase base que representa a una persona vinculada a la universidad."""


class Persona:
    def __init__(self, identificacion, nombre, correo):
        self.__identificacion = self._validar_texto(identificacion, "La identificación")
        self.__nombre = self._validar_texto(nombre, "El nombre")
        self.__correo = self._validar_correo(correo)

    @staticmethod
    def _validar_texto(valor, campo):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"{campo} no puede estar vacío.")
        return valor.strip()

    @staticmethod
    def _validar_correo(correo):
        if not isinstance(correo, str) or not correo.strip() or "@" not in correo:
            raise ValueError("El correo debe ser válido y no puede estar vacío.")
        return correo.strip()

    def get_identificacion(self):
        return self.__identificacion

    def set_identificacion(self, identificacion):
        self.__identificacion = self._validar_texto(identificacion, "La identificación")

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = self._validar_texto(nombre, "El nombre")

    def get_correo(self):
        return self.__correo

    def set_correo(self, correo):
        self.__correo = self._validar_correo(correo)

    def mostrar_informacion(self):
        print(f"Identificación: {self.__identificacion}")
        print(f"Nombre: {self.__nombre}")
        print(f"Correo electrónico: {self.__correo}")

    def realizar_actividad_principal(self):
        print(f"{self.__nombre} realiza actividades en la universidad.")
