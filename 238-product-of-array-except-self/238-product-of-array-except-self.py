class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1,2,3,4]
        1 - 2,3,4
        2 - 1,3,4
        3 - 1,2,4
        4 - 1,2,3
        
        dp[0] = prod of all other elements - 2*3*4
        dp[n] = prod of all elements until that - 1*2*3
        dp[1] = dp[1-1] * dp[1+1:n]
        dp[2] = (nums[2-1]*dp[1-1]) * (dp[1+1:n]/nums[2])
        ...
        dp[m] = (nums[m-1] * dp[m-1])%nums[2]
        """
        #with division and dp
        # n = len(nums)
        # if n == 0:
        #     return []
        # if n == 1:
        #     return nums
        # dp = [1] * n
        # #base case
        # for i in range(1,n):
        #     dp[0] *= nums[i]
        # for i in reversed(range(n-1)):
        #     dp[n-1] *= nums[i]
        # # print(dp)
        # for i in range(1,n-1):
        #     if nums[i] != 0:
        #         dp[i] = (nums[i-1] * dp[i-1])//nums[i]
        #     else:
        #         dp[i] = nums[i-1] * dp[i-1]
        # return dp
    
        #dp without division
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return nums
        fwd, bwd = [0] * n, [0] * n
        fwd[0] = 1
        bwd[n-1] = 1
        for i in range(1,n):
            fwd[i] = fwd[i-1]* nums[i-1]
        for i in reversed(range(n-1)):
            bwd[i] = bwd[i+1]* nums[i+1]
        print(fwd, bwd)
        return [fwd[i]* bwd[i] for i in range(len(fwd))]