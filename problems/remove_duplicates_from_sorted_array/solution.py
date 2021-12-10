class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 0:
            return len(nums)
        else:
            m = 0
            i = 1
            while i < len(nums) - m:
                    if nums[i] == nums[i-1]:
                        n = nums.pop(i)#popping
                        nums.append(n)#appending to the end of the array
                        m += 1
                    else:
                        i += 1
        return len(nums) - m