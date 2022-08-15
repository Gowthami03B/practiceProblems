class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        low, high = 0, n-1
        if nums[high] > nums[0]:
            return nums[0]
        while(low <= high):
            mid = low + (high-low)//2
            if nums[mid] > nums[mid + 1]:
                return nums[mid+1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[0]:
                low = mid + 1
            else:
                high = mid - 1
                