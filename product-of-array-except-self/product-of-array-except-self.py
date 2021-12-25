class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = 1
        n = len(nums)
        ans = []
        ans.append(suffix)
        for i in range(1,n):
            ans.append(nums[i - 1] * ans[i - 1])
        for i in reversed(range(n)):
            ans[i] = ans[i] * suffix
            suffix *= nums[i]
        return ans