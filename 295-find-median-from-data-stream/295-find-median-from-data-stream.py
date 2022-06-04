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

"""
If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
1) create hashmap for 1 to 100
2) count values for each number
3) if total values is odd, then median value -findkth(size//2+1), size//2+1 is the mid value in an odd number array, we check when the count of values is >= size//2 + 1 and return it
4) if total values is even, (self.findkth(size // 2 + 1) + self.findkth(size // 2))/2

Time complexity - addNum - O(1), findMedian - O(100)
Space - O(100)

If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
1) create hashmap for 1 to 101 and for all values >100, count under 101
same as above
Time complexity - addNum - O(1), findMedian - O(100)
Space - O(101)

class MedianFinder:
    def __init__(self):
        self.counter = {i: 0 for i in range(1, 102)} #dictionary
        
    def addNum(self, num):
        if num <= 100:
            self.counter[num] += 1
        else:
            self.counter[101] += 1#Bucket sorting. Key=101 is to store the outliner values that greater than 100.
        print(self.counter)
            
    def findMedian(self):
        size = sum(self.counter.values()) #total number of values
        if size % 2 == 1: #odd count middle value
            return self.findkth(size // 2 + 1)
        else:
            return 0.5 * (self.findkth(size // 2 + 1) + self.findkth(size // 2))
        
    def findkth(self, k):
        count = 0
        for i in range(1, 102):#for i in range(1,100)
            count += self.counter[i] #count the total number of values
            if count >= k: #if count >= mid value, return i (the median value)
                return i

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(5)
obj.addNum(7)
obj.addNum(10)
obj.addNum(20)
param_2 = obj.findMedian()
print(param_2)
    """