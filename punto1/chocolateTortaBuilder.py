from tortabuilder import TortaBuilder
from torta import Torta

class ChocolateTortaBuilder(TortaBuilder):
    def __init__(self):
        self.torta = Torta()
        
    def preparar_masa(self):
        self.torta.set_masa("chocolate")
    
    def preparar_relleno(self):
        self.torta.set_relleno("dulce de leche")
    
    def obtener_torta(self):
        return self.torta