class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans,sum1 = nums[0],nums[0]
        
        for i in nums[1:] :
            sum1 = max(i,sum1+i)
            ans = max(ans, sum1)
        return ans
                
        