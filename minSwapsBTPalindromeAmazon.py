"""
Give a binary string consisting of 0's and 1's only. E.g., 0100101. We are allowed to pick
any two indexes and swap them. We have to return the minimum number of swaps required to make
it a palindrome or -1 if it cannot. The string 0100101 can be made a palindrome by swapping
(3,4)-> 0101001 and swapping (0,1) -> 1001001 which is a palindrome. In this case, the
correct answer is 2.

0100101
compare 1st and last, mismatch - note it
travel inward - 10010, compare 1st and last, mismatch - note it
travel inward - 001, compare 1st and last, mismatch - note it

even len and odd difference - cannot be a palindrome, 1110
even len and even difference - 1100 - 2 diff, 1 swap
odd len and even difference - 11100 - 2 diff, 1 swap (second 1 and last 0)
odd len and odd difference -11010 10101 - 1 diff, 2 swaps
"""
def minSwapsBTPalindrome(s):
    n = len(s)
    diff = 0
    i,j = 0, n-1
    while(i < j):
        if s[i] != s[j]:
            diff += 1
        i += 1
        j -= 1
    
    if diff % 2 !=0 and n%2 ==0:
        return -1
    return (diff+1)//2

print(minSwapsBTPalindrome("1110"))
