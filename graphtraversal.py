import networkx as nx
from graph2 import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)
