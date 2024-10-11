from tortabuilder import *
from torta import *

class VainillaTortaBuilder(TortaBuilder):
    def __init__(self):
        self.__torta = Torta()

    def preparar_masa(self):
        self.__torta.set_masa("vainilla")

    def preparar_relleno(self):
        self.__torta.set_relleno("dulce de leche")

    def obtener_torta(self):
        return self.__torta