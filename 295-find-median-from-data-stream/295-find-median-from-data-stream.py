from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.nums = []
        self.minHeap = [] #min heap to store large elements
        self.maxHeap = [] #max heap to store small elements

        #cannot take abs as there will be negative numbers also
    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -1 * num)
        #check if elements in maxHeap > minHeap, then take max ele from maxheap and move to minheap
        if self.maxHeap and self.minHeap and abs(self.maxHeap[0]) > self.minHeap[0]:
            heappush(self.minHeap, -1 * heappop(self.maxHeap))
            
        if len(self.maxHeap) > (len(self.minHeap) + 1):
            #take max ele from maxheap and move to minheap
            heappush(self.minHeap, -1 * heappop(self.maxHeap))
        
        if len(self.minHeap) > (len(self.maxHeap) + 1):
            #take max ele from maxheap and move to minheap
            heappush(self.maxHeap, -1 * heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        return (self.minHeap[0] + -1 * self.maxHeap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()