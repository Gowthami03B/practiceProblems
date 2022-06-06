class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, i = 0,0 #start=window start
        maxLen = 0
        for i in range(len(nums)):
            if nums[i] == 0: #if encounter 0, decrement K
                k -= 1
            while(k < 0): #when k becomes less than 0, we need to slide our window
                if nums[start] == 0:#if first element is 0, adjust k, if we slide the window and disregard this 0, need to increment k
                    k += 1
                start += 1#slide window by 1 position
            maxLen = max(maxLen, i - start + 1) #find maxLength
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
       