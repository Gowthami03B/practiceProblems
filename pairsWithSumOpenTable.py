"""
Given an array of N integers, and a number sum, the task is to find the number of pairs of integers in the array whose sum is equal to sum.

Examples:  

Input:  arr[] = {1, 5, 7, -1}, sum = 6
Output:  2
Explanation: Pairs with sum 6 are (1, 5) and (7, -1).

Input:  arr[] = {1, 5, 7, -1, 5}, sum = 6
Output:  3
Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5).         

Input:  arr[] = {1, 1, 1, 1}, sum = 2
Output:  6
"""
def pairsWithSum(arr,target):
    if not arr:
        return 0
    arr_map = {}
    count = 0
    for i in range(len(arr)):
        if target - arr[i] in arr_map:
            count += arr_map[target-arr[i]]
        if arr[i] in arr_map:
            arr_map[arr[i]] += 1
        else:
            arr_map[arr[i]] = 1
    return count

arr=[1,1,1,1]
target=2
print(pairsWithSum(arr,target))
