class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sub = max_sub = nums[0]
        for num in nums[1:]:
            current_sub = max(num,num + current_sub)
            max_sub = max(current_sub, max_sub)
        return max_sub