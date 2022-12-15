from heapq import heappush
fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")
print("The fruits are: ", fruits)

from heapq import heappop
heappop(fruits)
print("The fruits that still available are : ", fruits)