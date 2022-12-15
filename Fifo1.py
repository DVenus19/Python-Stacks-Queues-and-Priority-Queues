from queues2 import Queue
fifo = Queue("1st","2nd","3rd")
print("The numbers of queues is ", len(fifo))


for element in fifo:
    print(element)

    print("the number of current queues is ", len(fifo))