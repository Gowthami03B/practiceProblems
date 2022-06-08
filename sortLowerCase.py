"""
Problem: Given an input string, return an output string such that all the lower case characters should be sorted. Indices of non-lower case characters should remain the same as in the original input string.

Eg. Input -> 'Test@123 Google'
Output -> 'Teeg@123 Gloost'

"""
from string import ascii_lowercase
from heapq import heappush, heappop
def sortLowerCase(s):
    heap = []
    res = [""] * len(s)
    for c in s:
        if c in ascii_lowercase:
            heappush(heap, c)
    print(heap)

    for idx, c in enumerate(s):
        if c in ascii_lowercase:
            res[idx] = heappop(heap)
        else:
            res[idx] = c

    return "".join(res)

s = "Test@123 Google"
print(sortLowerCase(s))
