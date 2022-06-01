class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        extra space
        res = []
        for i in range(len(nums)):
            res.append(sum(nums[:i+1]))
        return res
        """
        #without extra space, you just have to add to the prev sum
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums