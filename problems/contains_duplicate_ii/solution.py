class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_map = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in num_map:
                diff = i - num_map[nums[i]]
                if diff <= k:
                    return True
            num_map[nums[i]] = i
        return False