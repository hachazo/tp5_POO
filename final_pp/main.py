from reportero import *
from sistemameteorologico import *

def main():
    reportero1 = Reportero("Juan", 25)
    reportero2 = Reportero("Pedro", 30)
    reportero3 = Reportero("Maria", 20)
    
    sistema = SistemaMeteorologico("Sistema Meteorologico")
    sistema.add_reporteros(reportero1)
    sistema.add_reporteros(reportero2)
    sistema.add_reporteros(reportero3)
    
    sistema.notificar()

if __name__ == "__main__":
    main()