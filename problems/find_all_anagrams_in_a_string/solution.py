from collections import defaultdict
class Solution:
    #your approach is also commendable, you were able to try it with two pointers, but 
    #it would never work in cases where a substring has chars from p but not all and so on
    #"cbaebabacd","abc", only getting [0]
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         n = len(s)
#         m = len(p)
#         map = defaultdict(int)
#         psorted = sorted(p)
#         for c in p:
#             map[c] += 1
        
#         i,j = 0,0
#         res = []
#         while j < n:
#             if s[j] in map and j - i < m:
#                     if sorted(s[i:j+1]) == psorted and j < n:
#                         res.append(i)
#                         i += 1
#                         j -= 1
#                     else:
#                         j += 1
#             else:
#                         j += 1
#                         i = j
#         return res
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        pcount, scount = [0] * 26, [0] * 26
        for c in p:
            pcount[ord(c) - ord('a')] += 1
        res = []
        for i in range(n):
            scount[ord(s[i]) - ord('a')] += 1#increment count
            if i >= m:#when i >= len(p), slide window, remove count of first character to compare in groups of "p"
                scount[ord(s[i-m]) - ord('a')] -= 1
            if pcount == scount: #when both arrays are equal, return i-m+1(plus 1 bcs i is not incremented)
                res.append(i-m+1)
        return res