class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        #similar to rotated sorted array
        if n == 1:
            return nums[0]
        low, high = 0, n-1
        if nums[high] > nums[0]:
            return nums[0]
        while(low <= high):
            mid = low + (high-low)//2
            if nums[mid] > nums[mid + 1]:#find the pivot index where either mid > mid+1 or mid-1 > mid, those will be the smallest
                return nums[mid+1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[0]:#if mid > start, then search in right, else left
                low = mid + 1
            else:
                high = mid - 1
                