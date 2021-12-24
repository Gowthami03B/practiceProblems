from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        window = defaultdict(int)
        for i in range(n):
            if(nums[i] in window):
                return [i, window[nums[i]]]
            else:
                window[target - nums[i]] = i
        return s

        