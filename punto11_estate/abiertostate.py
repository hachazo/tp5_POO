from cajainterface import *

class CajaAbierta(Estadocaja):
    
    def get_estado(self):
        return "Abierta"
    
    def atender(self, edad: int):
        print("Atendiendo al cliente próximo en la fila.")