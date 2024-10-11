from abc import ABC, abstractmethod

class InterfaceArchivo(ABC):

    @abstractmethod
    def mostrar(self):
        pass