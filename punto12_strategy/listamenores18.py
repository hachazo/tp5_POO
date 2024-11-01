from strategy import *

class ListaMenores18(Filtro):
    
    def filtrar(self,catalogo):
        for pelicula in catalogo:
            if pelicula.get_clasificacion < 18:
                return pelicula