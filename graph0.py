from typing import NamedTuple
import networkx as nx


class City(NamedTuple):
    name: str
    country: str
    year: int
    latitude: float
    longitude: float

