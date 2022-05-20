import heapq
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        charmap = defaultdict(int)
        for c in s:
            charmap[c] += 1
        heap = []
        for char, freq in charmap.items():
            heapq.heappush(heap, (-freq,char))
        res = ""
        while heap:
            freq, char = heapq.heappop(heap)
            res += abs(freq) * char
        return res