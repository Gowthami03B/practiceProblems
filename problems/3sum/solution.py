class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i, j = 0,1
        # n = len(nums)
        # if n < 3:
        #     return []
        # nums.sort()
        # res = set()
        # for i in range(n - 2):
        #     for j in range(i+1, n-1):
        #         rem = -nums[i] - nums[j]
        #         s, l = j+1, n-1
        #         while(s <= l):
        #             mid = (s+l)//2
        #             if(nums[mid] == rem):
        #                 res.add((nums[i],nums[j],nums[mid]))
        #                 break
        #             elif(nums[mid] < rem):
        #                 s = mid + 1
        #             else:
        #                 l = mid - 1
        # return [list(ele) for ele in res]
        
        n = len(nums)
        nums.sort()
        res = []
        if n < 3:
            return []
        for i in range(n):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twosum(nums, i, res)
        return res
    def twosum(self,nums: List[int], i: int, res: List[List[int]]):
            lo,hi = i+1, len(nums)-1
            while(lo < hi):
                sum = nums[i] +  nums[lo] +  nums[hi]
                if sum == 0 :
                    res.append([ nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -=1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                elif sum < 0:
                    lo += 1
                else:
                    hi -= 1
    
                        
                        