class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        charmap = collections.OrderedDict()
        longest = 0
        start = 0
        if k == 0 and len(s) >= 1:
            return 0
        for i in range(len(s)):
            charmap[s[i]] = i
            if len(charmap) == k:
                longest = max(longest, i - start + 1)
            while len(charmap) > k:
                if start in charmap.values():
                    del charmap[s[start]]
                start += 1
        return longest if longest > 0 else len(s)