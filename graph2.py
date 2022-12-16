from typing import NamedTuple
import networkx as nx
from queueMixin import Queue

class City(NamedTuple):
    name: str
    country: str
    year: int
    latitude: float

