class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # let's know left, the index of its first occurrence; and right, the index of its last occurrence. 
        left, right, count = {}, {}, defaultdict(int)
        for i, x in enumerate(nums):
            if x not in left: 
                left[x] = i #start indices of numbers
            right[x] = i#end occurrence of the same number
            count[x] += 1

        ans = len(nums)
        degree = max(count.values())#find degree of list
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)#last occurrence- first occurrence + 1

        return ans