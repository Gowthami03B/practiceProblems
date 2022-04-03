class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if not s and not t:
            return False
        elif not s and len(t) == 1:
            return True
        elif not t and len(s) == 1:
            return True
        if abs(len(s) - len(t)) > 1:
            return False
        if s == t:
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