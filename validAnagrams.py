class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        window = {}
        if len(s) != len(t):
            return False
        i = 0
        while i < len(s):
            if(s[i] in window):
                window[s[i]] += 1
            else:
                window[s[i]] = 1
            i+= 1
        i = 0
        while i < len(t):
            if(t[i] not in window):
                return False
            else:
                window[t[i]] -= 1
            i+=1
        return all(value == 0 for value in window.values())

    def isAnagramsSorting(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
s = "aacc"
t = "caac"
print(Solution().isAnagramsSorting(s,t))
