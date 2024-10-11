class Torta:
    def __init__(self):
        self.__masa = ""
        self.__relleno = ""
        
    def set_masa(self, masa):
        self.__masa = masa
    
    def set_relleno(self, relleno):
        self.__relleno = relleno
        
    def __str__(self):
        return f"Torta con masa de: {self.__masa}  y relleno: {self.__relleno}"