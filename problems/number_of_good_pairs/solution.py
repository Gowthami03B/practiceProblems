from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numMap = defaultdict(int)
        for num in nums:
            numMap[num] += 1
        res = 0
        for key,val in numMap.items():
            res += (val * (val - 1))//2
        return res
            
        