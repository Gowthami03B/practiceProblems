from heapq import heappush, heappop
class StockPrice:

    def __init__(self):
        self.timestamp_prices = {}
        self.maxTime = 0
        self.maxHeap = []
        self.minHeap = []

    def update(self, timestamp: int, price: int) -> None:
        self.timestamp_prices[timestamp] = price
        self.maxTime = max(self.maxTime, timestamp)
        
        heappush(self.maxHeap, (-price, timestamp))
        heappush(self.minHeap, (price, timestamp))

    def current(self) -> int:
        return self.timestamp_prices[self.maxTime]

    def maximum(self) -> int:
        topPrice, topTime = heappop(self.maxHeap)
        while -topPrice != self.timestamp_prices[topTime]:
            topPrice, topTime = heappop(self.maxHeap)
        heappush(self.maxHeap, (topPrice, topTime))
        return -topPrice
    def minimum(self) -> int:
        topPrice, topTime = heappop(self.minHeap)
        while topPrice != self.timestamp_prices[topTime]:
            topPrice, topTime = heappop(self.minHeap)
        heappush(self.minHeap, (topPrice, topTime))
        return topPrice

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()