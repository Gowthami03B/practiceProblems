class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = []
        dp += cost #the first 2 base values are from cost itself.
        dp.append(0) #for the last step
        for i in range(2, n + 1):
            dp[i] += min(dp[i-1],dp[i-2]) #cost to reach that step is the min of i-1 and i-2 steps + curr step and for last step, it's 0
        return dp[n]
            