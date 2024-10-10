from tortabuilder import TortaBuilder
from torta import Torta

class CocoTortaBuilder(TortaBuilder):
    def __init__(self):
        self.torta = Torta()
    
    def preparar_masa(self):
        self.torta.set_masa("coco")
        
    def preparar_relleno(self):
        self.torta.set_relleno("dulce de leche")
    
    def obtener_torta(self):
        return self.torta