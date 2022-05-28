import heapq
from heapq import heappop, heappush
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
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
        
        