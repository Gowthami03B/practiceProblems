class Solution:
    def searchInsertBruteForce(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while(l <= r):
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target and mid == len(nums) - 1:
                return mid + 1
            elif nums[mid] > target and mid == 0:
                return mid
            elif nums[mid] > target and nums[mid - 1] < target:
                return mid
            elif nums[mid] < target and nums[mid + 1] > target:
                return mid + 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while(l <= r):
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        return l