from Game.core.entidades import Scene


def entradas_teclado (events, components, state, assets):
    pass


def actualizar(dt, components, state):
    pass


def renderizar(assets, components, screen, state):
    pass


def crear_escena(assets: dict, state: ResultState) -> Scene:
    def _entradas_teclado(events):
        return entradas_teclado(events=events, components=components, state=state, assets=assets)

    def _actualizar(dt):
        actualizar(dt=dt, components=components, state=state)

    def _renderizar(screen):
        renderizar(assets=assets["results"], components=components, screen=screen, state=state)
    def iniciar_componentes(assets):
        
    return Scene( entradas_teclado=_entradas_teclado,actualizar=_actualizar, renderizar=_renderizar)