"""
Electronic Exchange.
You work in an electronic exchange. Throughout the day, you receive ticks (trading data) which consists of product name and its traded volume of stocks. Eg: {name: vodafone, volume: 20}. What data structure will you maintain if:
* You have to tell top k products traded by volume at end of day. (HEAP and HashMap) is good enough right, as stocks come in, we add the data in map, and at the end of the day, push onto the minheap and when size  > k, we can pop, and high volume stocks are in the minheap
* You have to tell top k products traded by volume throughout the day. - Can use Heap, but need to pop from heap when size  > k and when value on heap is different from Map

You have to tell top k products traded by volume throughout the day.  - HEAP
"""
class StockStickersHeap:
   def __init__(self):
       self.stockmap=defaultdict(int)
       self.minheap = []
   def addToStream(self,stream):#O(log N), N elements then O(N log N)
       stream_list = stream.split(" ")
       for stream in stream_list:
           sticker, value = stream.split("|")
           value = int(value)
           self.stockmap[sticker] += value
           heappush(self.minheap,(self.stockmap[sticker],sticker))

   def fetchTopK(self,k):#O(N-k log N-k) ~ O(N log N)
       count = 0
       while len(self.minheap) > k:
           while self.minheap[0][0] != self.stockmap[self.minheap[0][1]]:
               heappop(self.minheap)
           heappop(self.minheap)
       print(self.minheap)

obj = StockStickersHeap()
obj.addToStream('MSFT|400 IBM|1000 AAPL|500 AAPL|600 NFLX|1000 AMZN|700 GOGL|300')
obj.addToStream('MSFT|550')
print(obj.fetchTopK(4)) #[(950, 'MSFT'), (1000, 'IBM'), (1100, 'AAPL'), (1000, 'NFLX')]
obj.addToStream('GOGL|1500')
print(obj.fetchTopK(1)) #[(1800, 'GOGL')]
obj.addToStream('IBM|100')
obj.addToStream('AAPL|300')
print(obj.fetchTopK(2))#[(1400, 'AAPL'), (1800, 'GOGL')]

#You have to tell top k products traded by volume throughout the day.  - SortedDict
from sortedcontainers import SortedDict
class StockStickers:
   def __init__(self):
       self.stockmap=defaultdict(list)
       self.sortedStockMap = SortedDict()
   def addToStream(self,stream): #Normally O(log N) for Sorted Dict, but since we want to remove sticker, O(N)
       stream_list = stream.split(" ")
       for stream in stream_list:
           sticker, value = stream.split("|")
           value = int(value)
           if sticker in self.stockmap:
               preValue = self.stockmap[sticker]
               countStocks = len(self.sortedStockMap.get(-preValue))
               if countStocks == 1:
                   del self.sortedStockMap[-preValue]
               else:
                   temp = self.sortedStockMap[-preValue]
                   temp.remove(sticker) #O(N)
               newValue = preValue + value
               self.stockmap[sticker] = newValue
               if not self.sortedStockMap.get(-newValue):
                   self.sortedStockMap[-newValue] = [sticker]
               else:
                   self.sortedStockMap[-newValue].append(sticker)
           else:
               self.stockmap[sticker] = value
               if not self.sortedStockMap.get(-value):
                   self.sortedStockMap[-value] = [sticker]#multiple stickers can have same value
               else:
                   self.sortedStockMap[-value].append(sticker)
 def fetchTopK(self,k): #O(K) iterate over K keys
       count = 0
       res = []
       for value, stickers in self.sortedStockMap.items():
           for sticker in stickers:
               res.append((sticker,-value))
               count += 1
               if count == k:
                   break
           if count == k:
               break
       return res
