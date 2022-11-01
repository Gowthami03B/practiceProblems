from collections import deque
class MyStack:

    def __init__(self):
        self.q1=deque()
        self.q2=deque()
        self.topEle = 0

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.topEle=x

    def pop(self) -> int:
        temp = deque()
        while len(self.q1) > 1:
            self.topEle=self.q1.popleft()
            self.q2.append(self.topEle)
        lastEle = self.q1.pop()
        self.q1= self.q2
        self.q2=temp
        return lastEle

    def top(self) -> int:
        return self.topEle

    def empty(self) -> bool:
        return False if len(self.q1) > 0 else True
        
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()