from Game.core import estados
from Game.core.entidades import Escena
from Game.core.estados import Estado_juego


def inicializar_componentes()-> dict:
    pass

def manejar_entradas (eventos, componentes, estado, recursos):
    pass


def actualizar(tiempo_delta, componentes, estado,recursos):
    pass


def renderizar(superficie, componentes, estados, recursos):
    pass

def crear_escena(recursos: dict, estado: Estado_juego) -> Escena:

    componentes = inicializar_componentes()

    def _manejar_entradas(eventos):
        return manejar_entradas(eventos=eventos, componentes=componentes, estado=estado, recursos=recursos)

    def _actualizar(tiempo_delta):
        actualizar(tiempo_delta=tiempo_delta, componentes=componentes, estado=estado,recursos=recursos)

    def _renderizar(screen):
        renderizar(superficie=screen, componentes=componentes, estados=estado, recursos=recursos)

    return Escena( manejar_entradas=_manejar_entradas,actualizar=_actualizar, renderizar=_renderizar)