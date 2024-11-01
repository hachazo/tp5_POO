from cajainterface import *

class CajaSuspendida(Estadocaja):
    
    def get_estado(self):
        return "Suspendida"
    
    def atender(self, edad: int):
        if edad >= 60:
            print("Atendiendo al cliente mayor de 60 años.")
        else:
            print("La caja está suspendida. Por favor, espere.")