## Circular Queue

"""
1. assign a None list with given length
2. initialize the position of head and tail as -1
3. enqueue: assign value to head position
4. dequeue: change value to tail position 
"""
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k
        self.head = 0
        self.tail = 0
        self.queue = [None] * k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.queue[self.tail] = value
        else:
            self.tail = (self.tail + 1) % self.capacity
            self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if not self.isEmpty():
            # self.queue.pop(self.head)
            if self.head != self.tail:
                self.queue[self.head] = None
                self.head = (self.head + 1) % self.capacity
            else:
                self.queue[self.head] = None
            return True
        else:
            return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if not self.isEmpty():
            front = self.queue[self.head]
            # self.head += 1
            return front
        else:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if not self.isEmpty():
            rear = self.queue[self.tail]
        # self.tail = (self.tail + self.size -1) % self.size
            return rear
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.tail == self.head and self.queue[self.head] == None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if (self.tail + 1) % self.capacity == self.head and self.queue[self.head] != None:
            return True
        else:
            return False
