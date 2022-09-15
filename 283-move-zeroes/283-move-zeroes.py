class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                s = i if s == -1 else s
                continue
            else:
                if s != -1:
                    nums[s] = nums[i]
                    nums[i] = 0
                    s += 1
                else:
                    continue
        
        