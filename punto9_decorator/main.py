from producto import *
from usdDecorator import *
from arsDecorator import *

producto = Producto("producto1",90000.50)

print("Precio original:", producto.get_precio())

producto_usd = USDDecorator(producto)
print("Precio en USD:", producto_usd.get_precio())

producto_ars = ARSDecorator(producto)
print("Precio en ARS:", producto_ars.get_precio())