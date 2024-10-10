class Director:
    def __init__(self, builder):
        self.__builder = builder

    def construir_torta(self):
        self.__builder.preparar_masa()
        self.__builder.preparar_relleno()

    def obtener_torta(self):
        return self.builder.obtener_torta()