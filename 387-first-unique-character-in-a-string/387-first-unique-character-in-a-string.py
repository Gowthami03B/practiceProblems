class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        # i = collections.Counter(1920120129102)
        # print(i)
        for i, val in enumerate(s):
            if count[val] == 1:
                return i
        return -1