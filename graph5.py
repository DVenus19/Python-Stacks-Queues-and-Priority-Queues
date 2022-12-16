from typing import NamedTuple
import networkx as nx
from queueMixin import Queue, Stack
from collections import deque

class City(NamedTuple):
    name: str
    country: str
    year: int
    latitude: float
    longitude: float
