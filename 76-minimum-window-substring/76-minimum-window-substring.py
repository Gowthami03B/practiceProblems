class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if m == n and s == t:
            return s
        if n > m: #if t < s, no solution
            return ""
        tMap = collections.defaultdict(int) #creating map for substring
        for char in t:
            tMap[char] += 1
        curr, count = 0, len(tMap) #length of chars from s in t, maintaining length of tMap for comparison(it's not t length but map length)
        minLength = math.inf
        start,end = 0,0
        sCurrMap = collections.defaultdict(int)#creating map for chars found in s which are in t
        i = 0
        for j in range(m):
            sCurrMap[s[j]] += 1#inc for each char
            #if curr char in tmap and counts match, then increment curr
            if s[j] in tMap and sCurrMap[s[j]] == tMap[s[j]]:
                curr += 1
            #once curr == count, i.e chars in s are in t
            # Try and contract the window till the point where it ceases to be 'desirable'.
            while i<=j and curr == count:
                if (j-i+1) < minLength: #update minLength if we are at a new minLength only
                    minLength = j-i+1
                    start,end = i,j
                sCurrMap[s[i]] -= 1 #we change our window size, subtracting the leftmost char
                if s[i] in tMap and sCurrMap[s[i]] < tMap[s[i]]:#but if the char we are removing is in t and because of shrinking window size, it's count in s becomes less than t, then we need to decrement our curr
                    curr -= 1
                i += 1#explanding window from left to find a new window
        return s[start:end+1] if minLength != math.inf else ""    
        
        
#     #fails for some cases "aaaaaaaaaaaabbbbbcdd","abcdd"
#     def minWindowBruteForce(self, s: str, t: str) -> str:
#         m = len(s)
#         n = len(t)
#         if m == n == 1 and s == t:
#             return s
#         if n > m: #if t . s, no solution
#             return ""
#         tMap = collections.defaultdict(int) #creating map for substring
#         for char in t:
#             tMap[char] += 1
#         sCurrMap = collections.defaultdict(int)#creating map for chars found in s which are in t
#         count = n #maintaining length of t for comparison
#         minLength = math.inf
#         minLengthIndices = collections.defaultdict(list)
#         # s,e = 0,0
#     #we go from start to end for each character
#         for i in range(len(s)):
#             for j in range(i,len(s)):
#                 if s[j] in tMap:
#                     sCurrMap[s[j]] += 1 #increment in sMap and decrement count
#                     count -= 1
#                 if count == 0:#if count is 0, check if maps are equal, if so update minLength and minLength indicies
#                     if tMap == sCurrMap:
#                         minLength = min(minLength, j-i+1) #update minLength
#                         minLengthIndices[j-i+1] = (i,j) #update minLength indices
#                     count = n #since we break here to increment i, reset count and sMap
#                     sCurrMap.clear()
#                     break
#                 elif j == m-1: #in case where j runs to end of string and nothing happens, we need to increment i then too, hence reset count, sMap
#                     count = n
#                     sCurrMap.clear()
#         if len(minLengthIndices) > 0:
#             start,end =minLengthIndices[minLength]
#         return s[start:end+1] if minLength != math.inf else "" #if minLength is not infinity, update string
    