from subscriberinterface import *
import random

class SistemaMeteorologico: # class SistemaMeteorologico(Subscriberinterface):
    def __init__(self, nombre):
        self.nombre = nombre
        self.reporteros = []
    
    def add_reporteros(self, reportero):
        self.reporteros.append(reportero)
    
    def remover_reporteros(self, reportero):
        self.reporteros.remove(reportero)
        
    def notificar(self):
        print("sistema meteorologico notifica a los reporteros")
        temperatura = random.randint(-10,40)
        
        for reportero in self.reporteros:
            reportero.reportar(temperatura)
