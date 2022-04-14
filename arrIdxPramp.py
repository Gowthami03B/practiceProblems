"""
Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the 
lowest index i for which arr[i] == i. 
Return -1 if there is no such index. 
Analyze the time and space complexities of your solution and explain its correctness.

Examples:

input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2

input: arr = [-1,0,3,6]
output: -1 # since no index in arr satisfies arr[i]
"""
#trick is to find the lowest index. bruteforce - loop all elements and check for first match (since it's already sorted)
#Improved - binary search

def arrIdx(nums):
    s , h = 0, len(nums) - 1
    midIdx = float('inf')
    while(s <= h):
        mid = (s+h)//2
        if(nums[mid] == mid):
            midIdx = min(midIdx, mid)
            h = mid - 1 #hence we move towards left once we found a match to see if there are matches before
        elif(nums[mid] > mid):
            h = mid - 1
        else:
            s = mid + 1
    return -1 if midIdx == float('inf') else mid
nums = [0,1,2,3,4,5,6,7,8] # in this example it matches 4 first, but we also have 0
print(arrIdx(nums))
