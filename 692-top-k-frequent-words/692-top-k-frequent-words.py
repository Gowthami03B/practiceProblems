import heapq
from heapq import heappop, heappush
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordMap = collections.defaultdict(int)
        res = []
        for word in words:
            wordMap[word] += 1
        maxheap = []
        for word, freq in wordMap.items():
            heappush(maxheap, (-freq, word))
        for _ in range(k):
            res.append(heappop(maxheap)[1])
        return res
        
        
        