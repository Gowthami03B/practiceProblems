import heapq
from collections import Counter
class Solution:
    def frequencySortNormal(self, s: str) -> str:
        charmap = Counter(s)
        print(charmap)
        # charmap = defaultdict(int)
        # for c in s:
        #     charmap[c] += 1
        res = ""
            
        for char, freq in charmap.most_common():
            print(char, freq)
            res += freq * char
        # heap = []
        # for char, freq in charmap.items():
        #     heapq.heappush(heap, (-freq,char))
        # while heap:
        #     freq, char = heapq.heappop(heap)
        #     res += abs(freq) * char
        return res
    
    def frequencySort(self, s: str) -> str:
        charmap = Counter(s)
        maxFreq = max(charmap.values())
        res = ""
        print(charmap)
        buckets = [[] for _ in range(maxFreq+1)]
        for char, freq in charmap.items():
            buckets[freq].append(char)
        print(buckets)
        for i in range(len(buckets)-1,0,-1):
            for c in buckets[i]:
                res += i * c
        return res
                
            