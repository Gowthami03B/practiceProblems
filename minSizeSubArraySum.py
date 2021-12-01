def minSizeSubArraySum(target, nums):
    start , sum = 0, 0
    result = float("inf") #infinity
    for i, val in enumerate(nums):
        sum += val
        while(sum >= target):
            result = min(result, i+1 - start)
            sum -= nums[start]
            start += 1
        
    return result if result != float("inf") else 0

nums = [2,3,1,2,4,3]
target = 7
print(minSizeSubArraySum(target, nums))
