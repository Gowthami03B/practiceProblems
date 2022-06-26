import heapq
from heapq import heappop, heappush
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordMap = collections.defaultdict(int)
        for word in words:
            wordMap[word] += 1
        maxheap = []
        for word, freq in wordMap.items():
            heappush(maxheap, (-freq, word))
        
        return [heappop(maxheap)[1] for _ in range(k)]
        
        
        
        