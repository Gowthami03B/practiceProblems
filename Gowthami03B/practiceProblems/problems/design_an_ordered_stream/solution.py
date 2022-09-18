class OrderedStream:

    def __init__(self, n: int):
        self.stream_set = set()
        self.stream={}
        self.last_added = -1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        self.stream_set.add(idKey)
        res= []
        i = idKey - 1
        if self.last_added == i or (self.last_added == -1 and idKey ==1):
            while i+1 in self.stream_set:
                res.append(self.stream[i+1])
                i += 1
            self.last_added = i
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)