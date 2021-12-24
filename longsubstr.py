#The time complexity is O(2n)=O(n) as in the worst case each character will be visited twice by left and right.
from collections import defaultdict
def longest_unique_substring(s):
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


#Given a string, find the length of the longest substring without repeating characters.
#The time complexity is O(n³) as we need O(n²) to list all substrings and for each substring, 
# we need O(n) to check if the characters are all unique or not.
def longestSubstr(str):
    def is_unique(start, end):
        charSet = set()
        for z in range(start, end):
            if str[z] in charSet:
                return False
            else:
                charSet.add(str[z])
        return True

    n = len(str)
    if n == 1:
        return n
    longest = float('-inf')
    for i in range(n):
        for j in range(i+1, n+1):
            if(is_unique(i, j)) :
                longest = max(longest, j - i)
    return longest

print(longest_unique_substring("abbde"))
