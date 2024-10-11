from creadorJuegos import *
from juegodigital import JuegoDigital

class CreadorJuegosDigitales(CreadorJuegos):
    def crear_juego(self,id,importe,precio_plataforma):
        return JuegoDigital(id, importe, precio_plataforma)