"""
1. initialize a None list with given length
2. if first element in, assign to 0 position, sum += value, num ++
    elif list not full, assign to continue position, sum += value, num ++
    elif full, replace head position to new value, sum changes, num = size
"""
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = [None] * size
        self.capacity = size
        self.head = None
        self.tail = None
        self.sum = 0
        self.num = 0
    def next(self, val: int) -> float:
        if self.head == self.tail == None:
            self.head = self.tail = 0
            self.q[self.head] = val
            self.sum += val
            self.num += 1
        elif self.head <= self.tail < self.capacity-1:
            self.tail = (self.tail + 1) % self.capacity
            self.q[self.tail] = val
            self.sum += val
            self.num += 1
        else:
            self.sum = self.sum - self.q[self.head] + val
            self.q[self.head] = val
            self.head = (self.head + 1) % self.capacity
            self.tail = (self.tail + 1) % self.capacity
            self.num = self.capacity
        return self.sum / self.num


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
