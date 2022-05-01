class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        #brute force solution
        # count = 0
        # if len(nums) < 3:
        #     return count
        # for i in range(len(nums)-2):
        #     for j in range(i+1,len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] +nums[k] < target:
        #                 count += 1
        # return count
        #sorting the array is also a solution because
# because after sorting, different numbers still have different indices and we can always arrange them in a way such that i<j<k. As an example,
# [3,6,2,5,1,4] (index: 0,1,2,3,4,5) after sorted will be [1,2,3,4,5,6] (index: 4,2,0,5,3,1).
# Let's say we want to pick the numbers [2, 4, 6].
# We can pick them in this order: 6, 2, 4 so that they appear in the original array in order.
        #Two pointers
        #[-2,0,1,3] = -2,0,1,3
        if len(nums) < 3:
            return 0
        sum = 0
        nums.sort()
        for i in range(len(nums)):
            sum += self.twoSumSmaller(nums, i + 1,target-nums[i])
        return sum
            
    def twoSumSmaller(self, nums, start, target):
            i,j = start,len(nums) - 1
            sum = 0
            while(i < j):
                if nums[i] + nums[j] < target:
                    sum +=j-i#if 1st and last sum < target, which means all in between also has sum < target
                    i += 1
                else:
                    j -= 1
            return sum
                