class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        window = {}
        n = len(nums)
        for i in range(n):
            if(nums[i] in window):
                return True
            else:
                window[nums[i]] = 1
                
        return False
            