##bruteforce
def highestSum(nums, k):
    n = len(nums)
    if n < k:
        return -1

    highest_sum = float('-inf')
    for i in range(n-k + 1):
        current_sum = 0
        for j in range(k):
            current_sum += nums[i + j]
        
        highest_sum = max(highest_sum, current_sum)
    
    return highest_sum

##optimal
def highestSumOpt(nums, k):
    n = len(nums)
    if n < k:
        return -1

    highest_sum = float('-inf')
    current_sum = 0
    for i in range(k):
        current_sum += nums[i]
    for j in range(n-k):
        highest_sum = max(highest_sum, current_sum)
        current_sum = current_sum - arr[j] + arr[k + j]
    
    return highest_sum

arr = [6, 5, 8, 3, 2, 1]
print(highestSumOpt(arr,3))
