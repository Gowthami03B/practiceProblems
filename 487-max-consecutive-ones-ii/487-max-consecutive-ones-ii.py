class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = 1 #can flip one zero
        start = 0
        maxLen = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                k -= 1
            while( k < 0):
                if nums[start] == 0:
                    k += 1
                start += 1
            maxLen = max(maxLen, i - start + 1)
        return maxLen