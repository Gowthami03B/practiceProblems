class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[[]]
        for i in range(len(nums)):
            res += [c + [nums[i]] for c in res]

        return res

