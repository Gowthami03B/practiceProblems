class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False