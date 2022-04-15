import sys
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        if(len(nums) < 2):
            return -1
        i , j = 0, len(nums) - 1
        maxSum = float('-inf')
        # maxSum = -sys.maxsize - 1
        while(i < j):
            if(nums[i] + nums[j] >= k):
                j -= 1
            elif nums[i] + nums[j] < k:
                maxSum = max(maxSum, nums[i] + nums[j])
                i += 1
        return -1 if maxSum < 0 else maxSum 