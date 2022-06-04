class Solution:
    def missingNumber1(self, nums: List[int]) -> int:
        
        #O(n2) time complexity - not acceptable
        for n in range(0, len(nums) + 1):
            if n not in nums: #in operation in list is O(n)
                return n
            
    def missingNumberSorting(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        if nums[-1] != len(nums):
            return len(nums)
        #O(n log n) time complexity - sorting far better
        for i in range(1, len(nums)):
            expected = nums[i-1] + 1
            if nums[i] != expected:
                return expected
            
    #O(n) time complexity, O(n) space
    def missingNumberSet(self, nums: List[int]) -> int:
        num_set = set(nums)
        for num in range(len(nums) + 1):
            if num not in num_set: #O(1)- in operation on set is O(1)
                return num
            
    #we know that sum of numbers from 1to n is n(n+1)/2
     #O(n) time complexity,fastest
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) #0 has no value, hence sum can be take as for 5 numbers
        expectedSum = (n * (n+1))//2
        actualSum = sum(nums)
        return expectedSum - actualSum