class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        minimum_ele = min(nums)
        for num in nums:
            count += num -minimum_ele
        return count