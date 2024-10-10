from VainillaTortaBuilder import *
from director import *

vainilla_builder = VainillaTortaBuilder()
director = Director(vainilla_builder)
director.construir_torta()
torta_vainilla = director.obtener_torta()
print(torta_vainilla)