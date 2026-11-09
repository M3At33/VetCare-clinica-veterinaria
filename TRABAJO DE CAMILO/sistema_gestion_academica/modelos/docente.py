"""Clase Docente: hereda los datos comunes de Persona."""


from modelos.persona import Persona


class Docente(Persona):
    def __init__(self, identificacion, nombre, correo, numero_empleado,
                 facultad, tipo_contratacion, horas_semanales):
        super().__init__(identificacion, nombre, correo)
        self.__numero_empleado = self._validar_texto(numero_empleado, "El número de empleado")
        self.__facultad = self._validar_texto(facultad, "La facultad")
        self.__tipo_contratacion = self._validar_texto(tipo_contratacion, "El tipo de contratación")
        self.__horas_semanales = self._validar_horas(horas_semanales)

    @staticmethod
    def _validar_texto(valor, campo):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"{campo} no puede estar vacío.")
        return valor.strip()

    @staticmethod
    def _validar_horas(horas):
        if not isinstance(horas, (int, float)) or isinstance(horas, bool) or not 0 < horas <= 80:
            raise ValueError("Las horas semanales deben ser mayores que cero y no superar 80.")
        return horas

    def get_numero_empleado(self):
        return self.__numero_empleado

    def set_numero_empleado(self, numero):
        self.__numero_empleado = self._validar_texto(numero, "El número de empleado")

    def get_facultad(self):
        return self.__facultad

    def set_facultad(self, facultad):
        self.__facultad = self._validar_texto(facultad, "La facultad")

    def get_tipo_contratacion(self):
        return self.__tipo_contratacion

    def set_tipo_contratacion(self, tipo):
        self.__tipo_contratacion = self._validar_texto(tipo, "El tipo de contratación")

    def get_horas_semanales(self):
        return self.__horas_semanales

    def set_horas_semanales(self, horas):
        self.__horas_semanales = self._validar_horas(horas)

    def mostrar_informacion(self):
        print("\nTIPO: DOCENTE")
        super().mostrar_informacion()
        print(f"Número de empleado: {self.__numero_empleado}")
        print(f"Facultad: {self.__facultad}")
        print(f"Tipo de contratación: {self.__tipo_contratacion}")
        print(f"Horas semanales: {self.__horas_semanales}")

    def realizar_actividad_principal(self):
        print(f"Actividad principal: orienta clases en la {self.__facultad}.")
