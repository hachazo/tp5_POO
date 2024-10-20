from cajainterface import *

class CajaCerrada(Estadocaja):

    def get_estado(self):
        return "Cerrada"
    
    def atender(self, edad: int):
        print("La caja está cerrada. No se puede atender a nadie en este momento.")