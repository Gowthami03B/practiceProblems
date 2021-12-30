import heapq
class Solution:
    def lastStoneWeight(self, nums: list[int]) -> list[int]:
        nums = [n*-1 for n in nums] #bcs heap returns the smallest elements
        heapq.heapify(nums)
        while len(nums) > 1:
            s1 = heapq.heappop(nums)
            s2 = heapq.heappop(nums)
            if(s1!=s2):
                heapq.heappush(nums, s1 - s2)

        return -heapq.heappop(nums) if nums else 0
    
    
#converting an array to heap in python takes O(N) time complexity and O(1) space complexity
#heap pop and push operations take O(Log N) - total - O(N log N)

