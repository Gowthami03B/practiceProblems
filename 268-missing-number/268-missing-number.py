class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for n in range(0, len(nums) + 1):
            if n not in nums:
                return n