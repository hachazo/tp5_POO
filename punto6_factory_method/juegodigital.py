from juego import *

class JuegoDigital(Juego):
    def __init__(self,id,importe,precio_plataforma):
        super().__init__(id, importe)
        self.__precio_plataforma = precio_plataforma

    def getprecio(self):
        return self._importe * self.__precio_plataforma