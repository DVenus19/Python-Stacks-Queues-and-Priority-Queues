from typing import NamedTuple
import networkx as nx
from queueMixin import Queue
from collections import deque

class City(NamedTuple):
    name: str
    country: str
    year: int
    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, attrs):
