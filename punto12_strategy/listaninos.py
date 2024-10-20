from strategy import *

class ListaNinos(Filtro):
        
        def filtrar(self,catalogo):
            for pelicula in catalogo:
                if pelicula.get_clasificacion < 13:
                    return pelicula