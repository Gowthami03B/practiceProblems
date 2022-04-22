class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #we traverse haystack once, hence O(N)
        #but we also create substrings from haystack of size needle, hence O(N)
        if len(needle) == 0 or len(haystack) == 0:
            return -1
        if haystack == needle:
            return 0
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if haystack[i:i+n] == needle:
                return i
        return -1
            