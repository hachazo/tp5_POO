from archivo import *
from carpeta import *


archivo1 = Archivo("archivo1")
archivo2 = Archivo("archivo2")
archivo3 = Archivo("archivo3")

carpeta1 = Carpeta("carpeta1")
carpeta1.agregar(archivo1)
carpeta1.agregar(archivo2)

carpeta2 = Carpeta("carpeta2")
carpeta2.agregar(archivo3)
carpeta2.agregar(carpeta1)

carpeta2.mostrar()