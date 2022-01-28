# Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index. Return -1 if the target is not in the array.

# Input:

# arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
# target = 3
# Output: 1

# Explanation: First occurrence of 3 is at index 1.

# Input:

# arr = [2, 3, 5, 7, 11, 13, 17, 19]
# target = 6
# Output: -1
from typing import List

def find_first_occurrence(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(arr)
    low , high = 0, n-1
    index = float("inf")
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            index = min(index,mid)
            high = mid - 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return index if index != float('inf') else -1

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = find_first_occurrence(arr, target)
    print(res)

