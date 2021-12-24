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

##2pointers
def highestSum2Pointers(nums, k):
    n = len(nums)
    if n < k:
        return -1

    left = 0
    right = k - 1
    highest_sum = float('-inf')
    while(right < n):
        current_sum = 0
        current_sum += arr[left] + arr[left + 1] + arr[right]
        left+= 1
        right+= 1
        highest_sum = max(highest_sum, current_sum)
    
    return highest_sum

##2pointers
def highestSum2Pointers1(nums, k):
    n = len(nums)
    if n < k:
        return -1

    left = 0
    current_sum = 0 
    right = 0
    highest_sum = float('-inf')
    while(right < n):
        current_sum += arr[right]
        right+=1
        if right-left == k:
            highest_sum = max(highest_sum, current_sum)
            current_sum -= arr[left]
            left+= 1
    
    return highest_sum

arr = [6, 5, 8, 3, 2, 1]
print(highestSum2Pointers1(arr,3))
