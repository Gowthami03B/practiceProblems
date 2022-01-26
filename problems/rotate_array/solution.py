class Solution:
    def reverse(self, nums: List[int], start : int, end: int) -> None:
        # #using extra array - Time complexity O(N), Space O(N)
        # n = len(nums)
        # new = [None] * n
        # k = k %n
        # for i in range(n):
        #     if i < n - k:
        #         new[i + k] = nums[i]
        #     else:
        #         new[i - k - 1] = nums[i]
        # nums[:] = new
        # #using shifting -  Time complexity O(N*k), Space O(1)
        # n = len(nums)
        # k %= n #when k > n, then number of shifts required is just k % n times
        # for i in range(k):
        #     prev = nums[-1]
        #     for j in range(n):
        #         nums[j], prev = prev, nums[j]
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start , end = start + 1, end - 1
    def rotate(self, nums: List[int],k:int) -> None:
        n = len(nums)
        k = k %n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        
    #using reverse Time complexity O(N), Space O(1)
        
        
            