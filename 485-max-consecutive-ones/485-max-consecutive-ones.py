class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxLen = 0
        # #approach 1 - when 0, move start of window by i + 1
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         start = i + 1 
        #     maxLen = max(maxLen, i - start + 1)
        # return maxLen
    
        #when 1, inc count, else find max and reset count. if there are continuous 1'st at end, need to find them too hence max(max,count)
        for i in range(len(nums)):
            if nums[i]:
                count += 1
            else:
                maxLen = max(maxLen, count)
                count = 0
        return max(maxLen,count)