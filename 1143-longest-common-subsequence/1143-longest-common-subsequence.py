from functools import lru_cache
class Solution:
    #memoization
    
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        """
        2 main points in solving this, abcde | ace
        if first 2 chars match res = 1+ LCS(rest of chars in t1 and t2)
        say bcade | ace
        if they don't match res = max(LCS(rest of t1 without first char, t2), LCS(t1, rest of t2 without first char))
        """
        @lru_cache(maxsize=None)
        def memo_solve(p1,p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1 + 1,p2 + 1)
            else:
                return max(memo_solve(p1,p2 + 1), memo_solve(p1 + 1,p2))
            
        return memo_solve(0,0)
    
    #dynamic programming
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row][col + 1], dp[row + 1][col])
        return dp[0][0]
        