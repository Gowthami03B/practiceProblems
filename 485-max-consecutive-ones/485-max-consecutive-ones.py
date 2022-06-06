class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxLen = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         start = i + 1 
        #     maxLen = max(maxLen, i - start + 1)
        # return maxLen
    
        for i in range(len(nums)):
            if nums[i]:
                count += 1
            else:
                maxLen = max(maxLen, count)
                count = 0
        return max(maxLen,count)