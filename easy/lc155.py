## Min Stack
## push, pop, top and getMin should be O(1)

class MinStack:
    """
    Algorithms:
    1. initialize an empty list s
    2. when push number, get the min of (mins, number) as mins, add (number, mins) to list s
    3. when pop out a number, if number == mins, mins = mins of list[-1]
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = None

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.mins = x
        self.mins = min(self.mins, x)
        self.stack.append((x, self.mins))

    def pop(self) -> None:
        num = self.stack.pop()[0]
        if num == self.mins:
            if len(self.stack) > 0:
                self.mins = self.stack[-1][1]
            else:
                self.mins = None
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.mins


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
