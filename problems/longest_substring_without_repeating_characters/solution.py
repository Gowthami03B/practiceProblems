from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
       #The time complexity is O(2n)=O(n) as in the worst case each character will be visited twice by left and right.
        n = len(s)
        if n==0:
            return 0
        longest = float('-inf')
        left =0
        right = 0
        window = defaultdict(int)
        while right < n:
            rightChar = s[right]
            window[rightChar] += 1
            right+= 1

            while window[rightChar] > 1:
                window[s[left]]-= 1
                left += 1
            longest = max(longest, right - left)
        return longest

        