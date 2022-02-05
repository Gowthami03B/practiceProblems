class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # n = len(arr)
        # left, right = 0, n - 1
        # while(left <= right):
        #     mid = (left+right)//2
        #     if arr[mid] == target:
        #         return mid
        #     elif arr[mid] > target:
        #         high = mid - 1
        #     else:
        #         low = mid + 1
        # return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1