class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start = 0
        maxLen = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                start = i + 1 
            maxLen = max(maxLen, i - start + 1)
        return maxLen