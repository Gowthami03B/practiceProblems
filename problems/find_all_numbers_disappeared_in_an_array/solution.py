from collections import defaultdict
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # res = defaultdict(int)
        ans = []
        # for num in nums:
        #     res[num] = 1
        # print(res)
        # for i in range(1,len(nums)+1):
        #     if i not in res:
        #         ans.append(i)
        # return ans
        
        arr = [0] * (len(nums) + 1)
        for num in nums:
            arr[num] = 1
        for i in range(1,len(nums)+1):
            if(arr[i] == 0):
                 ans.append(i)
        return ans