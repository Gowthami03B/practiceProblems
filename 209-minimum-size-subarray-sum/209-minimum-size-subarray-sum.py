class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float("inf")
        totsum = 0
        i,j = 0,0
        while(i <= j and j < len(nums)):
            totsum += nums[j]
            while totsum >= target:
                minLen = min(minLen, j - i + 1)
                totsum -= nums[i]
                i += 1
            j += 1
        return minLen if minLen != float("inf") else 0
                
            