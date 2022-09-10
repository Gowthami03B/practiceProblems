"""
Q2
You are given a string s. Consider the following algorithm applied to this string:

Take all the prefixes of the string, and choose the longest palindrome between them.
If this chosen prefix contains at least two characters, cut this prefix from s and go back to the first step with the updated string. Otherwise, end the algorithm with the current string s as a result.
Your task is to implement the above algorithm and return its result when applied to string s.

Note: you can click on the prefixes and palindrome words to see the definition of the terms if you're not familiar with them.

Example

For s = "aaacodedoc", the output should be solution(s) = "".

The initial string s = "aaacodedoc" contains only three prefixes which are also palindromes - "a", "aa", "aaa". The longest one between them is "aaa", so we cut if from s.
Now we have string "codedoc". It contains two prefixes which are also palindromes - "c" and "codedoc". The longest one between them is "codedoc", so we cut if from the current string and obtain the empty string.
Finally the algorithm ends on the empty string, so the answer is "".
For s = "codesignal", the output should be solution(s) = "codesignal".
The initial string s = "codesignal" contains the only prefix, which is also palindrome - "c". This prefix is the longest, but doesn't contain two characters, so the algorithm ends with string "codesignal" as a result.

For s = "", the output should be solution(s) = "".
https://leetcode.com/discuss/interview-question/801274/robinhood-coding-question-2
"""
def stringManipulation(s):

    def check_palindrome(start,end):
        return s[start:end+1] == s[start:end+1][::-1]
    
    l = len(s)
    e = l-1
    output_starts_from = 0

    while e>output_starts_from:
        # create a check_palindrome() function separately and call it here
        if check_palindrome(output_starts_from, e)==True:
            output_starts_from = e+1#then we need to remove the prefix until e
            e = l-1#change e to l-1
        else:
            e-=1#decrement the length by 1
    return s[output_starts_from:]

print(stringManipulation("aaacodedoc"))
