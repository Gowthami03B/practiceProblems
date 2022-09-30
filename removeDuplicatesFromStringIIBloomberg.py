"""
Write a function to crush candy in one dimensional board. In candy crushing games, groups of like items are removed from the board. In this problem, any sequence of 3 or more like items should be removed and any items adjacent to that sequence should now be considered adjacent to each other. This process should be repeated as many time as possible. You should greedily remove characters from left to right.

Example 1:

Input: "aaabbbc"
Output: "c"
Explanation:
1. Remove 3 'a': "aaabbbbc" => "bbbbc"
2. Remove 4 'b': "bbbbc" => "c"

Follow up -
What if you need to find the shortest string after removal?
Example:
Input: "aaabbbacd", instead of removing a in first attempt, need to remove b first and then a, to get cd
Output: "cd"
Explanation:
1. Remove 3 'b': "aaabbbacd" => "aaaacd"
2. Remove 4 'a': "aaaacd" => "cd"
"""

def removeDuplicatesString(s):
    stack = [['#',0]]
    k = 3
    for c in s:
        if stack[-1][0] == c:
            stack[-1][1] += 1
            if stack[-1][1] >= k:
                stack.pop()
        else:
            stack.append([c,1])
    return "".join(char*count for char,count in stack)

s="aaabbba"
# print(removeDuplicatesString(s))

def removeDuplicatesStringFollowUp(s):
    stack = [['#',0]]
    k = 3
    for c in s:
        if stack[-1][0] == c:
            stack[-1][1] += 1
            # if stack[-1][1] >= k:
            #     stack.pop()
        else:
            i = len(stack)-1
            update_prev = False
            while stack[i][1] >= k:
                if stack[i][0] == c:
                    update_prev = True
                    stack[i][1] += 1
                i-=1
            if not update_prev:
                stack.append([c,1])
    print(stack)
    return "".join(char*count for char,count in stack if (count >=1 and count < k))
s="aaabbba"
s1="aaabbbacd"
# print(ord('a')-ord('b'))
print(removeDuplicatesStringFollowUp(s1))
