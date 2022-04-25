# https://realpython.com/python-data-classes/
from dataclasses import dataclass


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


pos = Position("Oslo", 10.8, 59.9)
print(pos)
pos.lat
print(f"{pos.name} is at {pos.lat}°N, {pos.lon}°E")

#########################################################################################
## class containing a deck of cards
from typing import List


@dataclass
class PlayingCard:
    rank: str
    suit: str


@dataclass
class Deck:
    cards: List[PlayingCard]


queen_of_hearts = PlayingCard("Q", "Hearts")
ace_of_spades = PlayingCard("A", "Spades")
two_cards = Deck([queen_of_hearts, ace_of_spades])

#########################################################################################

from typing import Any

# type hint is mandatory when defining the fields in your data class
# if you do not want to add explicit types to your data class, use typing.Any
# type is not enforced at runtime
@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42


from math import asin, cos, radians, sin, sqrt


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (
            sin((phi_2 - phi_1) / 2) ** 2
            + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2) ** 2
        )
        return 2 * r * asin(sqrt(h))


oslo = Position("Oslo", 10.8, 59.9)
vancouver = Position("Vancouver", -123.1, 49.3)
oslo.distance_to(vancouver)

#########################################################################################
# https://docs.python.org/howto/unicode.html#unicode-literals-in-python-source-code
# https://en.wikipedia.org/wiki/Unicode_input

RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
SUITS = "♣ ♢ ♡ ♠".split()


def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


# default_factory to handle mutable default values.
# To use default_factory (and many other cool features of data classes), you need to use the field() specifier:
from dataclasses import dataclass, field
from typing import List


@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)


#########################################################################################
from dataclasses import dataclass, field


@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, metadata={"unit": "degrees"})
    lat: float = field(default=0.0, metadata={"unit": "degrees"})
