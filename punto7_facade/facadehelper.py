from traduccionhelper import *
from formatohelper import *

class FacadeHelper:
    def __init__(self):
        self.__traductor = TraduccionHelper()
        self.__formato = FormatoHelper()

    def traducir_palabra(self, palabra: str) -> str:
        return self.__traductor.traducir(palabra)

    def convertir_a_mayusculas(self, cadena: str) -> str:
        return self.__formato.convertir_mayusculas(cadena)

    def convertir_a_minusculas(self, cadena: str) -> str:
        return self.__formato.convertir_minusculas(cadena)