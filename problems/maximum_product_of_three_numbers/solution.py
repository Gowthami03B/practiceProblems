import numpy
class Solution:
    def maximumProduct(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        # n = heapq.nlargest(3, nums)
        # s = heapq.nsmallest(2, nums)
        # s.append(nums[-1])
        # return max(numpy.prod(n), numpy.prod(s))
        return max(arr[0] * arr[1] * arr[n - 1],
               arr[n - 1] * arr[n - 2] * arr[n - 3])