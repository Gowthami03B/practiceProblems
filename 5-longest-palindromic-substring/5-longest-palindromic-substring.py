class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     dp = [[0] * n for _ in range(n)]
    #     ans = ""
    #     maxSubstrLen = 1
    #     for i in range(n):
    #         dp[i][i] = 1
    #     for i in range(n-1):
    #         if s[i] == s[i+1]:
    #             dp[i][i+1] = 2
    #             if dp[i][i+1] > maxSubstrLen:
    #                 maxSubstrLen = 2
    #                 ans = s[i:i+2]
    #             # maxSubstrLen = max(2, maxSubstrLen)
    #     for i in reversed(range(n-1)): #need to calculate i+1,j-1 dps before its successor
    #         for j in range(i+1,n):
    #             if dp[i+1][j-1] !=0 and s[i] == s[j]:
    #                 dp[i][j] = j-i+1
    #                 if dp[i][j] > maxSubstrLen:
    #                     maxSubstrLen = max(j-i+1,maxSubstrLen)
    #                     ans = s[i:j+1]
    #     print(dp, maxSubstrLen,ans)
    #     # for m in range(len(dp)):
    #     #     for n in range(m,len(dp)):
    #     #         if dp[m][n] == maxSubstrLen:
    #     #             return s[m:n+1]
    #     return ans if len(ans) > 1 else s[0]
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.maxVal = 0
        self.start = 0
        for i in range(n):
            self.expandCenter(s,i,i)
            self.expandCenter(s,i,i+1)
        return s[self.start : self.start + self.maxVal]
        
    def expandCenter(self,s,lo,hi):
        while(lo >= 0 and hi < len(s)):
            if s[lo] != s[hi]:
                break
            lo -= 1 
            hi += 1
        if self.maxVal < hi - lo - 1:#because we are doing lo -= 1 and hi += 1 in above steps
            self.maxVal = hi - lo - 1
            self.start = lo+1
