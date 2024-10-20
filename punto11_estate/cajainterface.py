from abc import ABC, abstractmethod

class Estadocaja(ABC):
    
    @abstractmethod
    def get_estado(self):
        pass
    
    @abstractmethod
    def atender(self):
        pass