import functools
from functools import lru_cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # n = len(s)
        # if n < 1:
        #     return n
        # memo = {}
        # def aux(lo = 0, hi = len(s) - 1):
        #     key = (lo, hi)
        #     if key in memo:
        #         return memo[key]
        #     if lo > hi:
        #         return 0
        #     elif lo == hi:
        #         return 1
        #     elif s[lo] == s[hi]:
        #         memo[key] = 2 + aux(lo+1, hi - 1)
        #     else:
        #         memo[key] = max(aux(lo+1, hi), aux(lo, hi - 1))
        #     return memo[key]
        # return aux()
            
    #using LRU cache
        @lru_cache(maxsize=None)
        def aux(lo=0, hi=len(s)-1):
                if lo > hi:
                    return 0
                elif lo == hi:
                    return 1
                if s[lo] == s[hi]:
                    return 2 + aux(lo+1, hi-1)
                else:
                    return max(aux(lo+1, hi), aux(lo, hi-1))
        return aux()
