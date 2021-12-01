def maxSubArraySum(nums):
    sum = nums[0]
    max_so_far = nums[0] #infinity
    for i, val in enumerate(nums[1:]): ##starts array from index 1
        sum = max(val, sum + val)
        max_so_far = max(max_so_far, sum)
    return max_so_far

nums = [1]
print(maxSubArraySum(nums))


