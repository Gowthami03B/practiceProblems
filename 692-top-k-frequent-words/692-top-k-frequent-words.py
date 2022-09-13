import heapq
from heapq import heappop, heappush
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordMap = collections.defaultdict(int)
        for word in words:
            wordMap[word] += 1
        maxheap = []
        #heap takes care of sorting
        for word, freq in wordMap.items():
            heappush(maxheap, (-freq, word))
            # heappush(minheap, (freq, word))
        #     if len(minheap) > k:#advantage of min heap is O(n logk) and max heap is O(n log n) but here it messes order as these are lexicographically sorted
        #         heappop(minheap)
        # return [heappop(minheap)[1] for _ in range(k)][::-1]
        #list comprehensions
        return [heappop(maxheap)[1] for _ in range(k)]
        
        
    def topKFrequentMethod2(self, words: List[str], k: int) -> List[str]:
        wordMap = Counter(words)
        output = [x[0] for x in sorted(wordMap.items(), key=lambda kv:(-kv[1],kv[0]))[:k]]#gives a list sorted by words in frequency first and lexicographical next, selecting first k words
        print(output)
        heap, res = [],[]
        for word, freq in wordMap.items():
            heappush(heap, (-freq,word)) #constructing a max heap, heap also takes care of lexicographical order
        print(heap)
        for _ in range(k):
            freq, word = heappop(heap) #pops the smallest element first or smallest lexicographical word
            res.append(word)
            
        return res
        