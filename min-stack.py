class MinStack:
    def __init__(self):
        self.realStack = []
        self.minStack = []
        # monotonic stack

    def push(self, val: int) -> None:
        self.realStack.append(val)
        if self.minStack and val>self.minStack[-1]:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.realStack.pop()

    def top(self) -> int:
        return self.realStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]