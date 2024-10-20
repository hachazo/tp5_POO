from abiertostate import *
from suspendidostate import *
from cerradoestate import *

class Banco:
    def __init__(self, nombre_cajero: str):
        self.__nombre_cajero = nombre_cajero
        self.__estado_actual = CajaCerrada()

    def cambiar_estado(self, nuevo_estado):
        self.__estado_actual = nuevo_estado
        print(f"La caja ha cambiado su estado a: {nuevo_estado.get_estado()}")

    def atender_cliente(self, edad):
        print(f"Cajero {self.__nombre_cajero} atendiendo...")
        self.__estado_actual.atender(edad)
