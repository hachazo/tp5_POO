from listacompleta import *
from listamenores18 import *
from listaninos import *
from plataforma import *
from pelicula import *

plataforma = PlataformaStreaming(ListaCompleta())
plataforma.agregar_pelicula(Pelicula("Película A", 18))
plataforma.agregar_pelicula(Pelicula("Película B", 12))
plataforma.agregar_pelicula(Pelicula("Película C", 16))
plataforma.agregar_pelicula(Pelicula("Película D", 8))

    # Mostrar el catálogo completo
print("Catálogo completo:")
plataforma.mostrar_catalogo()

    # Cambiar a la estrategia para niños menores de 13
print("\nCatálogo para menores de 13 años:")
plataforma.cambiar_estrategia(ListaNinos())
plataforma.mostrar_catalogo()

    # Cambiar a la estrategia para menores de 18 años
print("\nCatálogo para menores de 18 años:")
plataforma.cambiar_estrategia(ListaMenores18())
plataforma.mostrar_catalogo()