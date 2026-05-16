import ctypes
import os
import pygame

from Game.core.entidades import Scene
from Game.system.Inicializador_recursos import cargar_recursos

from Game.Escenas import InicioScreen
from Game.system.base_de_datos import init_db

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FUENTES = os.path.join(BASE_DIR, "recursos", "Fuentes",)
MUSIC = os.path.join(BASE_DIR, "recursos", "Audio","Musica")
FX = os.path.join(BASE_DIR, "recursos", "Audio","FX")
TEXTURAS = os.path.join(BASE_DIR, "recursos", "Texturas")


SCREEN_SIZE = (1920, 1080)

def main():
    ctypes.windll.user32.SetProcessDPIAware()
    pygame.init()
    icono = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "recursos", "icon.png"))
    pygame.display.set_icon(icono)

    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("ESAI")
    assets = cargar_recursos()
    init_db()
    current_scene = InicioScreen.crear_escena(assets)

    clock = pygame.time.Clock()
    running = True

    while running:
        dt = clock.tick(60) / 1000.0
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

        # handle input
        result = current_scene.handle_input(events)
        if isinstance(result, Scene):
            current_scene = result

        # update
        result = current_scene.update(dt)
        if isinstance(result, Scene):
            current_scene = result

        # render
        screen.fill((0, 0, 0))
        current_scene.render(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()