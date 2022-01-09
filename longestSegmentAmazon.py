# Given an Array of bad numbers and a range of integers, how can I determine the longest segment of integers within that inclusive range that doesn't contain a bad number?

# For example, you are given the lower limit l = 3 and the upper limit r = 48, The array badNumbers = [37,7,22,15,49,60]. Segments without bad numbers are [3,6], [8,14], [16,21], [23,36] and [38,48]. The longest segment is [23,36] and it is 14 elements long.

# Problem : Function Description Complete the function goodStatement in the editor below. The function must return an integer denoting the length of the longest contiguous range of natural number in the range l to r, inclusive, which does not include any bad numbers.

# goodSegment has the following parameter(s): badNumbers[badNumbers[0],...badNumbers[n-1]]: an array of integers l: an integer, the lower bound, inclusive r: an integer, the upper bound, inclusive

# Constraints 1≤n≤105, 1≤badNumbers[i]≤109, badNumbers contains distinct elements
import math
class Solution:
    def longestSegment(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        maxDist = float('-inf')
        prev = lower -1
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1
            if prev + 1 <= curr - 1:
                maxDist = max(maxDist, ((curr - 1) - (prev + 1)+1))
                # print(maxDist)
            prev = curr
        return maxDist

nums = [37,7,22,15,49,60]
print(Solution().longestSegment(nums, 3, 48))
