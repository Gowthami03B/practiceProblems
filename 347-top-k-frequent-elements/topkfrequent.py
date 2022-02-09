import heapq
import collections
from collections import Counter
def topKFrequentElements(nums, k):
    if k == len(nums):
        return nums
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

nums = [1,1,2,2,2]
k=1
print(topKFrequentElements(nums,k))
