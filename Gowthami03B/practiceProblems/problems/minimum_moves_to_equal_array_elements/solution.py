class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        This approach is based on the idea that adding 1 to all the elements except one is equivalent to decrementing 1 from a single element
        say 3,4,3,6,6 - 34365 34364 34363 34353 etc
        """
        count = 0
        minimum_ele = min(nums)
        for num in nums:
            count += num -minimum_ele #no of decrement operations is element - min
        return count