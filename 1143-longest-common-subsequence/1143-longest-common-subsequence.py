from functools import lru_cache
class Solution:
    #memoization
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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
    
#     #dynamic programming
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        