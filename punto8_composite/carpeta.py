from interfaceArchivo import *

class Carpeta(InterfaceArchivo):
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__hijos = []
    
    def agregar(self, hijo):
        self.__hijos.append(hijo)

    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        for hijo in self.__hijos:
            hijo.mostrar()