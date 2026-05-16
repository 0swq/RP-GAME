from dataclasses import dataclass
from typing import Callable

import pygame

from Game.system.Inicializador_recursos import Textura


@dataclass(frozen=True)
class Escena:
    manejar_entradas: Callable
    actualizar: Callable
    renderizar: Callable


@dataclass(frozen=True)
class Jugador:
    sprite_idle:            tuple[Textura, Textura]
    sprite_atacar:          Textura
    sprite_defender:        Textura
    sprite_recibir_danio:    Textura
    sprite_recibir_defensa: Textura
    x: int
    y: int

    def dibujar(self, superficie: pygame.Surface, fase: str, frame_idle: int) -> None:
        match fase:
            case "IDLE":
                self.sprite_idle[frame_idle].dibujar(superficie, self.x, self.y)
            case "PREPARAR_ATAQUE":
                self.sprite_atacar.dibujar(superficie, self.x, self.y)
            case "PREPARAR_DEFENSA":
                self.sprite_defender.dibujar(superficie, self.x, self.y)
            case "DADO":
                self.sprite_atacar.dibujar(superficie, self.x, self.y)
            case "RECIBIR_DAÑO":
                self.sprite_recibir_danio.dibujar(superficie, self.x, self.y)
            case "RECIBIR_DEFENSA":
                self.sprite_recibir_defensa.dibujar(superficie, self.x, self.y)
            case _:
                self.sprite_idle[0].dibujar(superficie, self.x, self.y)


@dataclass(frozen=True)
class Enemigo:
    sprite_idle:          tuple[Textura, Textura]
    sprite_atacar:        Textura
    sprite_recibir_danio: Textura
    x: int
    y: int

    def dibujar(self, superficie: pygame.Surface, fase: str, frame_idle: int) -> None:
        match fase:
            case "IDLE":         self.sprite_idle[frame_idle].dibujar(superficie, self.x, self.y)
            case "ATACAR":       self.sprite_atacar.dibujar(superficie, self.x, self.y)
            case "RECIBIR_DAÑO": self.sprite_recibir_danio.dibujar(superficie, self.x, self.y)
            case _:              self.sprite_idle[0].dibujar(superficie, self.x, self.y)