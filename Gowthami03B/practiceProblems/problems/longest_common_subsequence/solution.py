from functools import lru_cache
class Solution:
    #memoization
    
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        """
        2 main points in solving this, abcde | ace
        if first 2 chars match res = 1+ LCS(rest of chars in t1 and t2)
        say bcade | ace
        if they don't match res = max(LCS(rest of t1 without first char, t2), LCS(t1, rest of t2 without first char))
        O(M.N) O(M.N) - time and space
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
    """
    Therefore, we often want to convert a top-down memoization approach into a bottom-up dynamic programming one 
    Remembering back to Approach above, there were two cases.

    The first letter of each string is the same.
    The first letter of each string is different.
    1) For the first case, we solve the subproblem that removes the first letter from each, and add 1. In the grid, this subproblem is always the diagonal immediately down and right
    2) For the second case, we consider the subproblem that removes the first letter off the first word, and then the subproblem that removes the first letter off the second word. In the grid, these are subproblems immediately right and below. (row+1,col) and (row, col+1)
    
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]#extra 0's for extra row and col
        for col in reversed(range(len(text2))):#we are building bottom up hence reversed and start with cols first
            for row in reversed(range(len(text1))):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row][col + 1], dp[row + 1][col])
        return dp[0][0]
    
    #doesn't work for "psnw", "vozsh" we exhaust s1 and finish execution
    def longestCommonSubsequence1(self, s1: str, s2: str) -> int:
        if len(s1) < len(s2):
            s1,s2 = s2,s1

        i = j = 0
        longest = 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j] :
                longest = max(longest, j+1)
                i +=1
                j +=1
            else:
                i +=1
        return longest

        