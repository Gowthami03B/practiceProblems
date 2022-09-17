from collections import defaultdict
from heapq import heappush,heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = defaultdict(int)
        for num in nums:
            num_map[num] += 1
            
        minheap = []
        for num, count in num_map.items():
            heappush(minheap,(count,num))
            if len(minheap) > k:
                heappop(minheap)
                
        return [heappop(minheap)[1] for _ in range(k)]