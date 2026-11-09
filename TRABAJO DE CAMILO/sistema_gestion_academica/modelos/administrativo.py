"""Clase Administrativo: hereda los datos comunes de Persona."""


from modelos.persona import Persona


class Administrativo(Persona):
    def __init__(self, identificacion, nombre, correo, numero_empleado,
                 dependencia, cargo, jornada):
        super().__init__(identificacion, nombre, correo)
        self.__numero_empleado = self._validar_texto(numero_empleado, "El número de empleado")
        self.__dependencia = self._validar_texto(dependencia, "La dependencia")
        self.__cargo = self._validar_texto(cargo, "El cargo")
        self.__jornada = self._validar_texto(jornada, "La jornada")

    @staticmethod
    def _validar_texto(valor, campo):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"{campo} no puede estar vacío.")
        return valor.strip()

    def get_numero_empleado(self):
        return self.__numero_empleado

    def set_numero_empleado(self, numero):
        self.__numero_empleado = self._validar_texto(numero, "El número de empleado")

    def get_dependencia(self):
        return self.__dependencia

    def set_dependencia(self, dependencia):
        self.__dependencia = self._validar_texto(dependencia, "La dependencia")

    def get_cargo(self):
        return self.__cargo

    def set_cargo(self, cargo):
        self.__cargo = self._validar_texto(cargo, "El cargo")

    def get_jornada(self):
        return self.__jornada

    def set_jornada(self, jornada):
        self.__jornada = self._validar_texto(jornada, "La jornada")

    def mostrar_informacion(self):
        print("\nTIPO: ADMINISTRATIVO")
        super().mostrar_informacion()
        print(f"Número de empleado: {self.__numero_empleado}")
        print(f"Dependencia: {self.__dependencia}")
        print(f"Cargo: {self.__cargo}")
        print(f"Jornada: {self.__jornada}")

    def realizar_actividad_principal(self):
        print(f"Actividad principal: trabaja como {self.__cargo} en {self.__dependencia}.")
