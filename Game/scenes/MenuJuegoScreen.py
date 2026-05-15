def crear_escena(assets: dict, state: ResultState) -> Scene:
    if state.win:
        save_data(state)
    components = init_components(assets["results"], state)

    def _handle_input(events):
        return handle_input(events=events, components=components, state=state, assets=assets)

    def _update(dt):
        update(dt=dt, components=components, state=state)

    def _render(screen):
        render(assets=assets["results"], components=components, screen=screen, state=state)

    return Scene(
        handle_input=_handle_input,
        update=_update,
        render=_render,
    )
