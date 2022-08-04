class MinStackSingleStack:

    def __init__(self):
        self.stack =[]

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            currentmin = self.stack[-1][1]
            self.stack.append((val,min(val,currentmin)))
            
    def pop(self) -> None:
        if self.stack:
            self.stack.pop() 

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

class MinStack:
    def __init__(self):
        self.stack =[]
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)            
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
            
    def pop(self) -> None:
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop() 
        self.stack.pop() 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()