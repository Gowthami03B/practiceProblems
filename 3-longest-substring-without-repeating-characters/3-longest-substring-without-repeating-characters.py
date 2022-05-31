class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        res = 0
        if not s:
            return res
        elif len(s.strip()) == 0 or len(s) == 1:
            return 1
        def check(l,m):
            window = {}
            for i in range(l,m + 1):
                if s[i] not in window:
                    window[s[i]] = 1
                else:
                    return False   
            return True
        
        for i in range(len(s)):
            for j in range(1,len(s)):
                if check(i,j):
                    res = max(res, j - i + 1)
        return res
    #BruteForce
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        if len(s) == 0:
            return longest
        elif len(s.strip()) == 0:
            return 1
        elif len(s) == 1:
            return 1
        for k in range(len(s)):
            i,j = k,k+1
            while(i < j and j < len(s)):
                if self.findRepeating(i,j,s):
                    longest = max(longest, j-i)
                    i += j
                else:
                     longest = max(longest, j-i+1)
                j += 1
        return longest if longest != 0 else len(s)
        
    def findRepeating(self,start, end, s):
            return s[end] in s[start:end]
