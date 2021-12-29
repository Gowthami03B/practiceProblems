import math
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        k = 3
        n = len(nums)
        diff = float('-inf')
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if(abs(sum - target) < abs(diff)):
                    diff = target - sum
                if sum < target:
                    left+= 1
                else:
                    right-= 1
            if diff == 0:
                break 
        return target - diff