from juego import *

class JuegoFisico(Juego):
    def __init__(self,id,importe, precio_traslado):
        super().__init__(id, importe)
        self.__precio_traslado = precio_traslado
        
    def getprecio(self):
        return self._importe + self.__precio_traslado