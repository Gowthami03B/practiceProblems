class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        left = right = sum = 0
        maxVal = float('-inf')
        for i in range(k):
            sum+= nums[i]
        maxVal = max(maxVal, sum)
        j = k
        for i in range(1,n-k + 1):
            sum = sum - nums[i-1] + nums[j]
            maxVal = max(maxVal, sum)
            j+=1
        return maxVal/k