from abc import ABC, abstractmethod

class Filtro(ABC):
    @abstractmethod
    def filtrar(self, catalogo: list) -> list:
        pass