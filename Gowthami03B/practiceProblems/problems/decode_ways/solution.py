from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp=[0] * len(s)#initialize to 0
        dp[0] = 1#for first string
        for i in range(1,len(s)):
            if s[i] != '0':#if s[i] is not a zero,then current decoding could be prev
                dp[i] = dp[i-1]
            
            if 10<= int(s[i-1:i+1]) <= 26:#Lets look at the number formed by s[i-1] and s[i], it could be between '01' to '99'. The only valid numbers are 10 -> 26.
                if i > 1:#consider 326, at i=2, we get 26, total ways would be dp[i]+=dp[i-2] i.e ways until dp[i-2]
                    dp[i] += dp[i-2]
                else:#case 226, 22 is valid when i==1, but can't add i-2, hence +1
                    dp[i] += 1
        return dp[-1]