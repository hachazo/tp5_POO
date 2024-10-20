class Pelicula:
    def __init__(self, titulo: str, clasificacion_edad: int):
        self.__titulo = titulo
        self.__clasificacion_edad = clasificacion_edad

    def get_clasificacion(self):
        return self.__clasificacion_edad
    
    def __str__(self):
        return f"{self.__titulo} (Clasificación: {self.__clasificacion_edad}+ años)"