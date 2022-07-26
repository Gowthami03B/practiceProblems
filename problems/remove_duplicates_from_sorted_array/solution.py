class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0;
        for j in range(i+1, len(nums)):
            if nums[i] != nums[j]:#whenever there is a mismatch
                i += 1#increment i (i will take the last index of the integer)
                nums[i] = nums[j]#copy nums[j] to i
        return i+1#all elements until i would be unique at the end of this operation