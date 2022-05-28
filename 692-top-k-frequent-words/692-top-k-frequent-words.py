import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         wordMap = Counter(words)
#         # wordMap = sorted(wordMap.items(), key=lambda kv:(-kv[1],kv[0]))
#         print(wordMap)
#         heap, res = [],[]
#         for word, freq in wordMap.most_common():
#             heappush(heap, (freq,word))
#             if len(heap) > k:
#                 heappop(heap)
#         while heap:
#             freq, word = heappop(heap)
#             res.append(word)
            
#         return res[::-1]
    
        lookup = collections.Counter(words)
        # heapify
        heap = []
        for key,val in lookup.items():
            heapq.heappush(heap,(-val,key))
			
        # pop out top k
        res = []        
        for i in range(k):
            neg_val,key = heapq.heappop(heap)
            res.append(key)

        return res
        
        