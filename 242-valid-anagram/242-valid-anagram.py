class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = [0] * 26
        for c in s:
            res[ord(c) - ord('a')] += 1
        for c in t:
            res[ord(c) - ord('a')] -= 1
        for v in res:
            if v >0 or v < 0:
                return False
        return True
