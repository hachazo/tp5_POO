from abc import ABC, abstractmethod

class TortaBuilder(ABC):
    
    @abstractmethod
    def preparar_masa(self):
        pass

    @abstractmethod
    def preparar_relleno(self):
        pass

    @abstractmethod
    def obtener_torta(self):
        pass
