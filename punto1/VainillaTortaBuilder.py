from tortabuilder import TortaBuilder
from torta import Torta

class VainillaTortaBuilder(TortaBuilder):
    def __init__(self):
        self.torta = Torta()

    def preparar_masa(self):
        self.torta.get

    def preparar_relleno(self):
        self.torta.relleno = "crema"

    def obtener_torta(self):
        return self.torta