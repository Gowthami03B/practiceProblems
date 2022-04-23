import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.heapify(nums)
        # print(nums)
        # print(heapq.nsmallest(k,nums),heapq.nsmallest(k,nums)[k-1])
        # print(heapq.nlargest(k,nums),heapq.nlargest(k,nums)[k-1])
        return heapq.nlargest(k,nums)[k-1]