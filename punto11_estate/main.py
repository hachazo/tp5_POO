from banco import *
from abiertostate import *
from suspendidostate import *
from cerradoestate import *

banco = Banco("Juan")

banco.atender_cliente(30)  # Caja cerrada

    # Abrir la caja
banco.cambiar_estado(CajaAbierta())
banco.atender_cliente(30)  # Caja abierta

    # Suspender la caja
banco.cambiar_estado(CajaSuspendida())
banco.atender_cliente(30)  # Caja suspendida, cliente joven
banco.atender_cliente(65)  # Caja suspendida, cliente mayor

    # Cerrar la caja
banco.cambiar_estado(CajaCerrada())
banco.atender_cliente(75) 
    