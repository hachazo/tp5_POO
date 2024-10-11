class TraduccionHelper:
    def __init__(self):
        self.__traducciones = {
            "hola": "hello",
            "mundo": "world",
            "gato": "cat",
            "perro": "dog",
            "casa": "house"
        }

    def traducir(self, palabra):
        return self.__traducciones.get(palabra.lower(), "Traducción no disponible")