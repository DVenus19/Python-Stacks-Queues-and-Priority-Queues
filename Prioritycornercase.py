from collections import deque
from heapq import heappop, heappush
from itertools import count

class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) >0:
            yield self.dequeue()




