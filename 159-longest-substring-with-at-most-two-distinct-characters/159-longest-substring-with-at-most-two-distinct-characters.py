class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0 or not s:
            return 0
        if len(s) < 3:
            return len(s)
        sMap = defaultdict(map) 
        start = longest = 0
        for end in range(len(s)):
            sMap[s[end]] = end
            longest = max(longest, end-start)
            if len(sMap) == 3:
                del_indx = min(sMap.values())
                del sMap[s[del_indx]]
                start = del_indx + 1
        longest = max(longest, end-start+1)

        return longest