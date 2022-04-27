from collections import defaultdict
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = defaultdict(int)
        ans = []
        for num in nums:
            res[num] = 1
        print(res)
        for i in range(1,len(nums)+1):
            if i not in res:
                ans.append(i)
        return ans