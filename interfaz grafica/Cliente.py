class Cliente:
    def __init__(self,codCliente = "",  nombre = "", dni = ""):
        self._codCliente = codCliente
        self._nombre = nombre
        self._dni = dni

    def getCod(self):
        return self._codCliente

    def getNombre(self):
        return self._nombre

    def getDni(self):
        return self._dni