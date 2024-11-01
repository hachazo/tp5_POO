from subscriberinterface import *

class Reportero:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def reportar(self, temperatura):
        print(f"El reportero {self.nombre} reporta temperatura de : {temperatura} grados")