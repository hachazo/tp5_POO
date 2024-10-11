from cocoTortaBuilder import *
from chocolateTortaBuilder import *
from VainillaTortaBuilder import *
from director import *

def hacer_torta(builder):
    director.set_builder(builder)
    director.construir_torta()
    return director.obtener_torta()

director = Director()
vainilla_builder = hacer_torta(VainillaTortaBuilder())
coco_builder = hacer_torta(CocoTortaBuilder())
chocolate_builder = hacer_torta(ChocolateTortaBuilder())
print(vainilla_builder)
print(coco_builder)
print(chocolate_builder)


# vainilla_builder = VainillaTortaBuilder()
# director = Director(vainilla_builder)
# director.construir_torta()
# torta_vainilla = director.obtener_torta()
# print(torta_vainilla)

# coco_builder = CocoTortaBuilder()
# director = Director(coco_builder)
# director.construir_torta()
# torta_coco = director.obtener_torta()
# print(torta_coco)


# chocolate_builder = ChocolateTortaBuilder()
# director = Director(chocolate_builder)
# director.construir_torta()
# torta_chocolate = director.obtener_torta()
# print(torta_chocolate)