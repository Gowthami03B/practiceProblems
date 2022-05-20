from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.heapify(nums)
        # print(nums)
        # print(heapq.nsmallest(k,nums),heapq.nsmallest(k,nums)[k-1])
        # print(heapq.nlargest(k,nums),heapq.nlargest(k,nums)[k-1])
        # return heapq.nlargest(k,nums)[k-1]
        
        #Method 1
        # heap = []
        # for n in nums:
        #     heappush(heap,-n)
        # for i in range(k):
        #     res = heappop(heap)
        # return -res
    
        #Method 2
        heap, res = [], []
        for n in nums:
            heappush(heap,n)
            if len(heap) > k:
                heappop(heap)
        return heap[0]
            