class Director:
    def __init__(self):
        self.__builder = None

    def set_builder(self, builder):
        self.__builder = builder
        
    def construir_torta(self):
        self.__builder.preparar_masa()
        self.__builder.preparar_relleno()

    def obtener_torta(self):
        return self.__builder.obtener_torta()