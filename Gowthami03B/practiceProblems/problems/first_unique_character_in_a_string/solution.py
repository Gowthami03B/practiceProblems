class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_arr = [0]*26
        for c in s:
            s_arr[ord(c)-ord('a')] += 1

        for i,c in enumerate(s):
            if s_arr[ord(c)-ord('a')] == 1:
                return i
        return -1