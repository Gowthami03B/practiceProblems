class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.arr = []

    def next(self, val: int) -> float:
        if(len(self.arr) == self.size):
            self.arr.pop(0)
        self.arr.append(val)
        return sum(self.arr)/len(self.arr)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)