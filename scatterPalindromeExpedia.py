"""
Find all scatter palindrome strings inside given string. A scatter palindrome is defined as a string in which characters can be shuffled to obtain a palindrome.

Example:

Input: "aabb"
Output: [a, aa, aab, aabb, abb, b, bb]
"""
import itertools
from collections import defaultdict
def scatterPalindrome(input):
    output=[]
    def canFormPalindrome(s):
        """
        The string to be palindrome all the characters should occur an even number of times if 
        the string is of even length and at most one character can occur an odd number of times if 
        the string length is odd.
        """
        s_list = defaultdict(int)
        for i,c in enumerate(s):#add chars and del them
            if c in s_list:
                del s_list[c]
            else:
                s_list[c] = i
        if len(s) % 2 == 0 and len(s_list) == 0:#if even and palindrome, len is 0
            return True
        if len(s) % 2 != 0 and len(s_list) == 1:#if odd and palindrome, len is 1 (atleast 1 occurs odd times)
            return True
        return False

    for i in range(1,len(input)+1):#for the the length of the string  + 1(since we need to generate combinations)
        for j in itertools.combinations(input,i):#generated as tuple
            k=''.join(j)#get the combination
            if canFormPalindrome(k): #cannot check palindrome with reverse like this as string is jumbled
                k=''.join(sorted(k))#jumble the palindrome
                if k not in output and k !='':
                    output.append(k)
    return output

print(scatterPalindrome("aabb"))
