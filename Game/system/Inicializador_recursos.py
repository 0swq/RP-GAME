import os
from dataclasses import dataclass
from typing import Tuple

import pygame

#Estos imports son las rutas de las carpetas de los recursos que se definieron en el archivo main
#Las puse en main para poder reutilizarlas en todo el codigo

from Game.main import FUENTES,FX,MUSIC,TEXTURAS,BASE_DIR

#Estas son funciones utilitarias para cargar archivos de imagenes , fuente y el otro de sonido
def cargar_textura(nombre_archivo: str, ruta: str) -> pygame.Surface:
    return pygame.image.load(os.path.join(ruta, nombre_archivo)).convert_alpha()
def cargar_sonido(nombre_archivo: str, ruta: str) -> pygame.mixer.Sound:
    return  pygame.mixer.Sound(os.path.join(ruta, nombre_archivo))
def cargar_fuente(nombre_archivo: str, tamaño: int, ruta: str) -> pygame.font.Font:
    return pygame.font.Font(os.path.join(ruta, nombre_archivo), tamaño)



@dataclass(frozen=True)
class Musica:
    musica: pygame.mixer.Sound

    def reproducir(self, loop: bool = False) -> None:
        loops = -1 if loop else 0
        self.musica.play(loops=loops)

    def pausar(self) -> None:
        self.musica.stop()

    def reanudar(self) -> None:
        self.musica.play()

    def detener(self) -> None:
        self.musica.stop()

    def cambiar_volumen(self, nivel: float) -> None:
        self.musica.set_volume(max(0.0, min(1.0, nivel)))


@dataclass(frozen=True)
class Sonido_fx:
    sonido: pygame.mixer.Sound

    def reproducir(self) -> None:
        self.sonido.play()

    def detener(self) -> None:
        self.sonido.stop()

    def cambiar_volumen(self, nivel: float) -> None:
        self.sonido.set_volume(max(0.0, min(1.0, nivel)))

@dataclass(frozen=True)
class Textura:
    imagen: pygame.Surface
    nombre: str

    def obtener(self) -> pygame.Surface:
        return self.imagen

    def escalar(self, ancho: int, alto: int) -> pygame.Surface:
        return pygame.transform.scale(self.imagen, (ancho, alto))

    def dibujar(self, superficie: pygame.Surface, x: int, y: int, ancho: int | None = None, alto: int | None = None) -> pygame.Rect:
        if ancho is not None or alto is not None:
            w, h = self.imagen.get_size()
            nuevo_ancho = ancho if ancho is not None else int(w * (alto / h))
            nuevo_alto = alto if alto is not None else int(h * (ancho / w))
            imagen = imagen = pygame.transform.smoothscale(self.imagen, (nuevo_ancho, nuevo_alto))
        rect = self.imagen.get_rect(topleft=(x, y))
        superficie.blit(self.imagen, rect)
        return rect

@dataclass(frozen=True)
class Fuente:
    fuente: pygame.font.Font
    color:  tuple[int, int, int]|None
    def dibujar(self, superficie: pygame.Surface,texto: str,x: int,y: int,color: tuple[int, int, int] | None = None) -> pygame.Rect:
        superficie_texto = self.fuente.render(texto, True, color or self.color)
        rect = superficie_texto.get_rect(topleft=(x, y))
        superficie.blit(superficie_texto, rect)
        return rect
    def dibujar_centrado(self, superficie: pygame.Surface,texto: str,cx: int,cy: int, color: tuple[int, int, int] | None = None,) -> pygame.Rect:
        superficie_texto = self.fuente.render(texto, True, color or self.color)
        rect = superficie_texto.get_rect(center=(cx, cy))
        superficie.blit(superficie_texto, rect)
        return rect


#Funciones de carga
def cargar_texturas_() -> dict[str, Textura]:
    return {
        "fondo_pelea": Textura(imagen=cargar_textura("fondo_pelea.png", TEXTURAS), nombre="fondo_pelea"),
    }

def cargar_musica_() -> dict[str, Musica]:
    return {
    }

def cargar_fx_() -> dict[str, Sonido_fx]:
    return {
    }

def cargar_fuentes_() -> dict[str, Fuente]:
    return {
        "ui": Fuente(fuente=cargar_fuente("zeropixel-eye-fs.otf", 24, FUENTES)),
    }

# Este dataclass sirve para cargar poder unificar todos los recursos en uno
@dataclass(frozen=True)
class Recursos:
    musicas:  dict[str, Musica]
    texturas: dict[str, Textura]
    sonidos:  dict[str, Sonido_fx]
    fuentes:  dict[str, Fuente]



# Este metodo crea el objeto recursos una sola vez para su uso en el juego
def cargar_recursos() -> Recursos:
    return Recursos(
            texturas=cargar_texturas_(),
            musicas=cargar_musica_(),
            sonidos=cargar_fx_(),
            fuentes=cargar_fuentes_(),
        )
