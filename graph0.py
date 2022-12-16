from typing import NamedTuple
import networkx as nx


class City(NamedTuple):
    name: str
    country: str
    year: int
    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, attrs):
        return cls(
            name=attrs["xlabel"],
