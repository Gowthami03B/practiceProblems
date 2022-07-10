class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit =0
        min_price = float("inf")#update min price as you see along the way, bcs you need to know the min price found so far to calculate max profit
        for i in range(len(prices)):
            if prices[i] < min_price:#update min price as u find it
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price 
        return max_profit
            