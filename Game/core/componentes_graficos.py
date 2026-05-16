from dataclasses import dataclass
import pygame

from Game.system.Inicializador_recursos import Fuente, Textura

DEBUG = False  # Esto activa y desactiva el borde rojo alrededor de los componentes, úsenlo para debugear


@dataclass
class Boton:
    normal: Textura
    hover: Textura
    x: int
    y: int
    centrado: bool = False

    @property
    def rect(self) -> pygame.Rect:
        if self.centrado:
            return self.normal.imagen.get_rect(center=(self.x, self.y))
        return pygame.Rect(self.x, self.y, self.normal.imagen.get_width(), self.normal.imagen.get_height())

    def esta_encima(self, mouse: tuple) -> bool:
        return self.rect.collidepoint(mouse)

    def dibujar(self, superficie: pygame.Surface) -> None:
        mouse = pygame.mouse.get_pos()
        textura = self.hover if self.esta_encima(mouse) else self.normal
        textura.dibujar(superficie, self.x, self.y)

        if DEBUG:
            pygame.draw.rect(superficie, (255, 0, 0), self.rect, 1)
            pygame.draw.circle(superficie, (0, 255, 0), (self.x, self.y), 4)


@dataclass
class Etiqueta:
    fuente: Fuente
    texto: str
    x: int
    y: int
    color: tuple | None = None
    alineacion: str = "centro"

    def dibujar(self, superficie: pygame.Surface) -> None:
        match self.alineacion:
            case "centro":
                self.fuente.dibujar_centrado(superficie, self.texto, self.x, self.y, self.color)
            case "izquierda":
                self.fuente.dibujar(superficie, self.texto, self.x, self.y, self.color)

        if DEBUG:
            surf = self.fuente.fuente.render(self.texto, True, (255, 255, 255))
            rect = surf.get_rect(center=(self.x, self.y)) if self.alineacion == "centro" else surf.get_rect(
                topleft=(self.x, self.y))
            pygame.draw.rect(superficie, (255, 0, 0), rect, 1)
            pygame.draw.circle(superficie, (0, 255, 0), (self.x, self.y), 4)

    def actualizar_texto(self, nuevo_texto: str) -> "Etiqueta":
        return Etiqueta(self.fuente, nuevo_texto, self.x, self.y, self.color, self.alineacion)


@dataclass
class BarraVida:
    x: int
    y: int
    ancho: int
    alto: int
    vida_total: float
    vida_actual: float
    color_fondo: tuple
    color_vida: tuple
    borde_radio: int = 0
    centrado: bool = False

    @property
    def rect(self) -> pygame.Rect:
        if self.centrado:
            return pygame.Rect(self.x - self.ancho // 2, self.y - self.alto // 2, self.ancho, self.alto)
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, superficie: pygame.Surface) -> None:
        r = self.rect
        pygame.draw.rect(superficie, self.color_fondo, r, border_radius=self.borde_radio)
        alto_relleno = int(r.height * (self.vida_actual / self.vida_total))
        pygame.draw.rect(superficie, self.color_vida,
                         (r.x, r.y + r.height - alto_relleno, r.width, alto_relleno),
                         border_radius=self.borde_radio)

        if DEBUG:
            pygame.draw.rect(superficie, (255, 0, 0), r, 1)
            pygame.draw.circle(superficie, (0, 255, 0), (self.x, self.y), 4)

    def actualizar(self, nueva_vida: float) -> "BarraVida":
        return BarraVida(self.x, self.y, self.ancho, self.alto,
                         self.vida_total, nueva_vida,
                         self.color_fondo, self.color_vida, self.borde_radio, self.centrado)
