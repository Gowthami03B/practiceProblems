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
            sMap[s[end]] = end #store the last index of char
            longest = max(longest, end-start)
            if len(sMap) == 3:#when more than 2 distinct chars are present
                del_indx = min(sMap.values())#find the min index char to be deleted
                del sMap[s[del_indx]]
                start = del_indx + 1#start would be after the del_indx
        longest = max(longest, end-start+1)#this is for a case when 

        return longest