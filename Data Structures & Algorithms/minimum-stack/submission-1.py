class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []
        self.size = 0

    def push(self, val: int) -> None:
        
        if len(self.stack) == 0:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            self.stack.append(val)
            minVal = self.minStack[self.size-1]
            if minVal < val:
                self.minStack.append(minVal)
            else:
                self.minStack.append(val)
        self.size += 1

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            self.minStack.pop()
            self.size -= 1
            

    def top(self) -> int:
        return self.stack[self.size-1]

    def getMin(self) -> int:
        return self.minStack[self.size-1]

        
