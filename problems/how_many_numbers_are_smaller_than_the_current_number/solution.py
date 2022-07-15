class Solution:
    def smallerNumbersThanCurrent(self, nums1: List[int]) -> List[int]:
        nums = sorted(nums1)
        n = len(nums)
        counts = {}
        counts[nums[0]] = 0
        res = [0] * n
        duplicate = 0
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                res[i] = res[i-1] + duplicate + 1
                duplicate = 0
            elif nums[i] == nums[i-1]:
                res[i] = res[i-1]
                duplicate += 1
            counts[nums[i]] = res[i]
        # print(res, counts)
        return [counts[n] for n in nums1]