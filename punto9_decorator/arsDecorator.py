class ARSDecorator:
    def __init__(self, producto):
        self.__producto = producto

    def get_precio(self):
        return f"$ARS {self.__producto.get_precio()}"