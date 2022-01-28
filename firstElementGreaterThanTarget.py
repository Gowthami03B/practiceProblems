# Given an array of integers sorted in increasing order and a target, find the index of the first element in the array that is larger than or equal to the target. Assume that it is guaranteed to find a satisfying number.

# Input:

# arr = [1, 3, 3, 5, 8, 8, 10]
# target = 2
# Output: 1

# Explanation: the first element larger than 2 is 3 which has index 1.

# Input:

# arr = [2, 3, 5, 7, 11, 13, 17, 19]
# target = 6
# Output: 3

from typing import List

def first_not_smaller(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(arr)
    low , high = 0, n-1
    index = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= target:
            index = mid
            high = mid - 1
        else:
            low = mid + 1
    return index

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = first_not_smaller(arr, target)
    print(res)
