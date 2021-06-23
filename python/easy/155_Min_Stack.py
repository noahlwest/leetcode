class MinStack:

    def __init__(self):
        self.data = []
        self.minimum = float('inf')
        

    def push(self, val: int) -> None:
        self.data.append(val)
        
        if self.minimum is not None and val < self.minimum:
            self.minimum = val
        elif self.minimum is None:
            self.minimum = val
        

    def pop(self) -> None:
        print(self.data)
        length = len(self.data)
        if length > 0:
            if self.data[length-1] == self.minimum:
                self.data.pop()
                if len(self.data) > 0:
                    self.minimum = min(self.data, default=None)
                else:
                    self.minimum = None
            else:
                self.data.pop()
                
    def top(self) -> int:
        length = len(self.data)
        if length > 0:
            return self.data[length-1]
        return

    def getMin(self) -> int:
        if self.minimum is None:
            return
        return self.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()