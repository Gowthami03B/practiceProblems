"""
Given an array of integers a, your task is to count the number of pairs i and j (where 0 ≤ i < j < a.length), such that a[i] and a[j] are digit anagrams.

Two integers are considered to be digit anagrams if they contain the same digits. In other words, one can be obtained from the other by rearranging the digits (or trivially, if the numbers are equal). For example, 54275 and 45572 are digit anagrams, but 321 and 782 are not (since they don't contain the same digits). 220 and 22 are also not considered as digit anagrams, since they don't even have the same number of digits.

Example

For a = [25, 35, 872, 228, 53, 278, 872], the output should be solution(a) = 4.

There are 4 pairs of digit anagrams:

a[1] = 35 and a[4] = 53 (i = 1 and j = 4),
a[2] = 872 and a[5] = 278 (i = 2 and j = 5),
a[2] = 872 and a[6] = 872 (i = 2 and j = 6),
a[5] = 278 and a[6] = 872 (i = 5 and j = 6).
Input/Output

[execution time limit] 6 seconds (py3)

[input] array.integer a

An array of non-negative integers.

Guaranteed constraints:
1 ≤ a.length ≤ 105,
0 ≤ a[i] ≤ 109.

https://leetcode.com/discuss/interview-question/798439/robinhood-coding-question-1
"""
import collections
from collections import defaultdict
def digitAnagramsCodeSignal(a):
    num_map = defaultdict(int)
    count = 0
    for num in a:
        x = num
        num_list = []
        while(x):
            temp = x%10
            x = x//10
            num_list.append(temp)
        
        num_list.sort()
        if tuple(num_list) in num_map:
            # print(num, tuple(num_list))
            count += 1
        else:
            num_map[tuple(num_list)] = 1
    count += len(a) - len(set(a))
    return count
    
a = [25, 35, 872, 228, 53, 278, 872]
print(digitAnagramsCodeSignal(a))
