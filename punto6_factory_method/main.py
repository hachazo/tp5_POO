from creadorJuegosfisicos import *
from creadorjuegosdigitales import *

creador_fisico = CreadorJuegosFisicos()
juego_fisico = creador_fisico.crear_juego(1, 50.0, 10.0)
print(f"Juego Físico - Precio Total: {juego_fisico.getprecio():.2f}")

# Crear un juego digital con un precio de plataforma de 1.15
creador_digital = CreadorJuegosDigitales()
juego_digital = creador_digital.crear_juego(2, 50.0, 1.15)
print(f"Juego Digital - Precio Total: {juego_digital.getprecio():.2f}")