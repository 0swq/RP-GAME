from dataclasses import dataclass



@dataclass(frozen=True)
class Estado_juego:
    turno:str
    puntaje:int
    vida_jugador:float
    vida_enemigo:float
    danio_jugador:float
    danio_enemigo:float
    defensa_jugador:float
    resultado_dado:int