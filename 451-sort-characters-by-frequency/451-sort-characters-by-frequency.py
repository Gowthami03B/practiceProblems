import heapq
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        charmap = Counter(s)
        print(charmap)
        # charmap = defaultdict(int)
        # for c in s:
        #     charmap[c] += 1
        res = ""
        for char, freq in charmap.most_common():
            res += freq * char
        # heap = []
        # for char, freq in charmap.items():
        #     heapq.heappush(heap, (-freq,char))
        # while heap:
        #     freq, char = heapq.heappop(heap)
        #     res += abs(freq) * char
        return res