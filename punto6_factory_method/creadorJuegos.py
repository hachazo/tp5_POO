from abc import ABC, abstractmethod

# Clase abstracta para la creación de juegos
class CreadorJuegos(ABC):
    @abstractmethod
    def crear_juego(self,id,importe,extra):
        pass