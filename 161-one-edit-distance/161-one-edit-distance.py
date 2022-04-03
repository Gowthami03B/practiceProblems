class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        i = 0;
        while(i < len(s) and i < len(t)):
            if(s[i] != t[i]):
                if len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                elif len(s) > len(t):
                    return s[i+1:] == t[i:]
                else:
                    return s[i:] == t[i+1:]
            i += 1
        return True
    #solution that saves space
#     def isOneEditDistance(self, s, t):
#         if abs(len(s) - len(t)) > 1 or s == t:
#             return False
        
#         found_inequality = False
#         i = j = 0
        
#         while i < len(s) and j < len(t):
#             if s[i] != t[j]:
#                 if found_inequality: return False
#                 found_inequality = True
#                 if len(s) < len(t): i -= 1
#                 elif len(s) > len(t): j -= 1
#             i += 1
#             j += 1
        
#         return True
