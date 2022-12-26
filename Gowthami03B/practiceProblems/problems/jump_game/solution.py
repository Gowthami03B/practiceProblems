class Solution:
    def canJump1(self, nums: List[int]) -> bool:
        #At each index we check maximum reacheable distance found till now and more forward, maxDistReacheable should be greater than the current index, if not, then return False

        maxDistReacheable = nums[0]
        for i in range(1,len(nums)):
            if(i > maxDistReacheable):
                return False
            maxDistReacheable = max( maxDistReacheable, i + nums[i] )
        return True
    
    
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if nums[0] == 0 and n > 1:
            return False
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n - 1):
            dp[i] = max(dp[i - 1] - 1, nums[i]) #max distance we can jump at an index is max(current val, prev val), prev val is the distance that can be jumped from prev step - 1 (say prev val is 3, can jump 3 steps from prev val , so if one jump is made, there are 2 more steps that can be done.)
            if dp[i] < 1 :#if dp[i] becomes < 1, no steps can be made from here and hence False
                return False
        return True