from interfaceArchivo import *

class Archivo(InterfaceArchivo):
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
    