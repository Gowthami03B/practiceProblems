class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(1, len(nums)):
            self.nums[i] += self.nums[i - 1]
        print(nums)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right] - self.nums[left-1] if left else self.nums[right] #if left is 0, then nums[right] is ans, else total sum until right - all the sum before left which is left -1


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)