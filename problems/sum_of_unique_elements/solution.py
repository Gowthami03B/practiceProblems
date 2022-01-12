class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        if(len(set(nums))== len(nums)):
            return sum(nums)
        if(len(set(nums)) == 1):
            return 0
        visit = set()
        repeat = set()
        for num in nums:
            if num in visit:
                repeat.add(num)
            else:
                visit.add(num)
        return sum(visit - repeat)