class Solution:
    """
        clarification qs - valid range of input
        neg numbers?
        does the subsequence needs to be consecutive?
        what happens when there are duplicate values?
        work through test cases with examples
        """
    def lengthOfLIS1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        dp = [1] * len(nums)#base case - bcs technically from every index, we can start an increasing subsequence
        #start with 1
        for j in range(1,len(nums)):
            for i in range(0, j):#go and check backwards to see what is the largest subsequence upto here
                if nums[i] < nums[j]:#if prev val < curr, subsequence possible and it will be the max of prev values + 1(for curr value)
            #hence max b/w curr val and prev val + 1
                    dp[j] = max(dp[j] , dp[i]+ 1)
        return max(dp)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        #binary search
        sub = []
        for num in nums:
            i = bisect_left(sub, num)#gets the position in sub where num can be inserted to maintain sorted order
            if i == len(sub):#when increasing order is happening and num > sub[-1]
                sub.append(num)
            else:#when we found a smaller element than sub[-1], replace sub[i] with num to maintain sorted order
                sub[i] = num
        return len(sub)
    
    def lengthOfLISBruteForce(self, nums: List[int]) -> int:
        #fails for [0,1,0,3,2,3],we can pick 0,1,3 - 3 len or 0,1,2,3 - 4 len
        #this is when you realize it's dynamic programming
        maxLen = 0
        for i in range(len(nums)):
            cnt = 0
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    cnt += 1
                    i = j
                else:
                    continue
            maxLen = max(maxLen, cnt + 1)
        return maxLen