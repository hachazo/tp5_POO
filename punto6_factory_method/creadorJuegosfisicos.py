from juegofisico import *
from creadorJuegos import *

class CreadorJuegosFisicos(CreadorJuegos):
    def crear_juego(self,id,importe,precio_traslado):
        return JuegoFisico(id, importe, precio_traslado)