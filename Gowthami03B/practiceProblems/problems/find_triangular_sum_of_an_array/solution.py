class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def calculateSum(nums):
            if len(nums) == 1:
                return nums[0]
            for i in range(len(nums)-1):
                nums[i] = (nums[i] + nums[i+1])%10
            nums.pop()
            return calculateSum(nums)
                
        return calculateSum(nums)