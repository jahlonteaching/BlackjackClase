from dataclasses import dataclass, field
from typing import ClassVar, Optional

CORAZON = "\u2764\uFE0F"
TREBOL = "\u2663\uFE0F"
DIAMANTE = "\u2666\uFE0F"
ESPADA = "\u2660\uFE0F"
TAPADA = "\u25AE\uFE0F"


@dataclass
class Carta:
    PINTAS: ClassVar[list[str]] = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    VALORES: ClassVar[list[str]] = [CORAZON, TREBOL, DIAMANTE, ESPADA]
    pinta: str
    valor: str
    tapada: bool = field(default=False, init=False)


class Mano:

    def __init__(self, cartas: tuple[Carta, Carta]):
        self.cartas: list[Carta] = []
        self.cartas.extend(cartas)

    def es_blackjack(self) -> bool:
        pass

    def agregar_carta(self, carta: Carta):
        pass

    def calcular_valor(self) -> int:
        pass

    def destapar(self):
        pass


class Baraja:

    def __init__(self):
        self.cartas: list[Carta] = [Carta(pinta, valor) for valor in Carta.VALORES for pinta in Carta.PINTAS]

    def revolver(self):
        pass

    def repartir_carta(self, tapada=False) -> Carta:
        pass


@dataclass
class Jugador:
    nombre: str
    fichas: int
    mano: Mano = field(default=None, init=False)

    def inicializar_mano(self, cartas: tuple[Carta, Carta]):
        pass

    def recibir_carta(self, carta: Carta):
        pass

    def agregar_fichas(self, fichas: int):
        pass

    def tiene_fichas(self) -> bool:
        pass


class Casa:

    def __init__(self):
        mano: Optional[Mano] = None

    def inicializar_mano(self, cartas: tuple[Carta, Carta]):
        pass

    def recibir_carta(self, carta: Carta):
        pass


class Blackjack:

    def __init__(self):
        self.apuesta_actual: int = 0
        self.jugador: Optional[Jugador] = None
        self.cupier: Casa = Casa()
        self.baraja: Baraja = Baraja()

    def registrar_usuario(self, nombre: str):
        pass

    def iniciar_juego(self, apuesta: int):
        pass

    def repartir_carta_a_jugador(self):
        pass

    def jugador_perdio(self) -> bool:
        pass

    def destapar_mano_de_la_casa(self):
        pass

    def casa_puede_pedir(self) -> bool:
        pass

    def repartir_carta_a_la_casa(self):
        pass

    def jugador_gano(self) -> bool:
        pass

    def casa_gano(self) -> bool:
        pass

    def hay_empate(self) -> bool:
        pass
