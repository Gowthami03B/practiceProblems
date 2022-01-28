# An array of boolean values is divided into two sections; the left section consists of all false and the right section consists of all true. Find the boundary of the right section, i.e. the index of the first true element. If there is no true element, return -1.

# Input: arr = [false, false, true, true, true]

# Solution-
# The binary decision we have to make when we look at an element is

# if the element is false, we discard everything to the left and the current element itself.
# if the element is true, the current element could be the first true although there may be other true to the left. We discard everything to the right but what about the current element?
# We can either keep the current element in the range or record it somewhere and then discard it. Here we choose the latter. We'll discuss the other approach in the alternative solution section.

from typing import List

def find_boundary(arr: List[bool]) -> int:
    n = len(arr)
    low,high = 0, n - 1
    index = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid]:
            index = mid
            high = mid -1 
        else:
            low = mid + 1
    return index

if __name__ == '__main__':
    arr = [x == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)
