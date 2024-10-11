from abc import ABC, abstractmethod

class Juego(ABC):
    def __init__(self, id, importe):
        self._id = id
        self._importe = importe

    @abstractmethod
    def getprecio(self):
        pass
    
    def notificar(self) -> str:
        notificador = self.factory_method()
        result = f"Creator: notifico al usuario con: {notificador.notificar_usuario()}"
        return result