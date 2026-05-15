from dataclasses import dataclass
from typing import Callable

@dataclass(frozen=True)
class Scene:
    entradas_teclado: Callable
    update: Callable
    render: Callable

@dataclass(frozen=True)
class entidad:
    x: int
    y: int

@dataclass(frozen=True)
class jugador:
    x: int
    y: int

@dataclass(frozen=True)
class enemigo:
    x: int
    y: int
