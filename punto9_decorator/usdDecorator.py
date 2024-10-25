class USDDecorator:
    def __init__(self, producto):
        self.__producto = producto

    def get_precio(self):
        # Agrega el símbolo $USD al precio del producto
        return f"$USD {self.__producto.get_precio()}"