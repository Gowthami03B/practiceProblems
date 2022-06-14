class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = []
        dp += cost
        dp.append(0)
        for i in range(2, n + 1):
            dp[i] += min(dp[i-1],dp[i-2])
        return dp[n]
            