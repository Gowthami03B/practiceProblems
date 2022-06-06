class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, i = 0,0 #start=window start
        maxLen = 0
        for i in range(len(nums)):
            if nums[i] == 0: #if encounter 0, increment count
                k -= 1
            while(k < 0): #when k becomes less than 0, we need to slide our window
                if nums[start] == 0:
                    k += 1
                start += 1
            maxLen = max(maxLen, i - start + 1)
        return maxLen
        
    def longestOnesMyApproach(self, nums: List[int], k: int) -> int:
        count0s = 0
        i, start = 0, 0
        maxLen = 0
        k1 = k
        while i < len(nums):
            if nums[i] == 0:
                if k == 0:
                    maxLen = max(maxLen, i - start) if i != len(nums) - 1 else max(maxLen, i - start + 1)
                    start = i
                    count0s = 1
                else:
                    count0s += 1
                    k -= 1         
            i+= 1
        return maxLen    
       