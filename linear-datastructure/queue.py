"""
-author : Vijay/am.vijay@gmail.com/Vijayraaghavan Manoharan
"""

# Queue - is a FIFO data structure implementation.
class Queue:
    __data = []

    # Add data into queue
    def enqueue(self,element):
        self.__data.append(element)
    
    # Fetch and Deletes data from Queue
    def dequeue(self):
        return self.__data.pop(0)

# Test
queue = Queue()
queue.enqueue("10")
queue.enqueue(5)
queue.enqueue("hello")

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
