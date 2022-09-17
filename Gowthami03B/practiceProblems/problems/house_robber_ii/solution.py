class Solution:
    def rob(self, nums: List[int]) -> int:
        #the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money. as the first and last houses are adjacent to each other
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:#if 2 houses, max of those
            return max(nums)
        #if 3 houses, since its a circle, then middle house or max(first and last)
        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))
                   
    def rob_simple(self,nums):#[1,3,1,3,100], [1,3,1,3] or [3,1,3,100], 3,3 or 1,100 or 3,100
        dp =[0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2],nums[i]+dp[i-2],nums[i]+dp[i-3])#max(last to last, curr + last to last, curr + last to last to last)
        return max(dp)
        