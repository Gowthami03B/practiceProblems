class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxdiff = 0
        minEle = float("inf")
        for i in range(len(nums)):
            if nums[i] < minEle:
                minEle = nums[i]
            if nums[i] - minEle > maxdiff:
                maxdiff = nums[i] - minEle
        return maxdiff if maxdiff != 0 else -1