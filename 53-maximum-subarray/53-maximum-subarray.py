class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxSum = float('-inf')
        for i in range(len(nums)):
            sum += nums[i]
            maxSum = max(sum, maxSum)
            if sum < 0:
                sum = 0
        return maxSum
                