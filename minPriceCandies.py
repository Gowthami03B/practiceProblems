"""
There is a candy store where multiple special new year deals are being offered for purchasing candies.
Luffy wants to buy some x number of candies from the store. Help Luffy in finding out minimum price at which he can purchase x number of candies.
1 candies for $2 (DEAL 'A')
3 candies for $5 (DEAL 'B')
7 candies for $9 (DEAL 'C')

Examples:

For 5 candies, the min price would be $9 (B + 2A) --> (B + 2A = $9) OR (5A = $10)
For 35 candies, the min price is $45
For 678 candies, the min price is $874
For 1245 candies, the min price is $1603
"""
from collections import defaultdict
def minPriceCandies(deals, noOfCandies):
    deals.sort()
    minPrice = float("inf")
    res = 0
    #similar to my thought process, but going by greedy approach, 
    # it's always when we go with the last deal, we get min price, we multiply quo with price, update candies count and repeat
    for i in reversed(range(len(deals))):
        if noOfCandies < deals[i][0]:
            continue
        quo = noOfCandies//deals[i][0]
        noOfCandies = noOfCandies%deals[i][0]
        res += quo * deals[i][1]
    return res
    
deals = [[1,2],[3,5],[7,9]]
print(minPriceCandies(deals,1245))
#O(deals)
