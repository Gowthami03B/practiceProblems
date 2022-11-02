from sortedcontainers import SortedList
#Use self balancing trees
class MaxStack:

    def __init__(self):
        self.stack = SortedList()
        self.maxstack = SortedList()#has sorted data
        self.cnt = 0

    def push(self, x: int) -> None:
        #index,value
        self.stack.add((self.cnt, x))#insertion order sorting based on id
        self.maxstack.add((x, self.cnt))#sorting based on value
        self.cnt += 1#maintain size of the list

    def pop(self) -> int:
        idx, val = self.stack.pop()
        self.maxstack.remove((val, idx))
        return val

    def top(self) -> int:
        return self.stack[-1][1]

    def peekMax(self) -> int:
        return self.maxstack[-1][0]

    def popMax(self) -> int:
        val, idx = self.maxstack.pop()
        self.stack.remove((idx, val))
        return val
    
import heapq
class MaxStack1:

    def __init__(self):
        self.heap = []
        self.cnt = 0
        self.stack = []
        self.removed = set()

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, (-x, -self.cnt))
        self.stack.append((x, self.cnt))
        self.cnt += 1

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        num, idx = self.stack.pop()
        self.removed.add(idx)
        return num

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        num, idx = heapq.heappop(self.heap)
        self.removed.add(-idx)
        return -num