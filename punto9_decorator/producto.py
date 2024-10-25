class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
    
    def get_precio(self):
        return f"{self.__precio:,.2f}"