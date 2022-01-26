class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_result = max_so_far = min_so_far = nums[0]
        
        for i in nums[1:]:
            temp_max_so_far = max(i, i*max_so_far, i*min_so_far)
            min_so_far = min(i, i*max_so_far ,i*min_so_far)
            
            max_so_far = temp_max_so_far
            max_result = max(max_result, max_so_far)
            
        return max_result