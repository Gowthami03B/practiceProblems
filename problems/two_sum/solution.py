class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_map = defaultdict(int)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in val_map:
                return [i, val_map[complement]]
            val_map[nums[i]] = i
        return []