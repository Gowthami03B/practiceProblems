class Solution:
    def longestValidParentheses1(self, s: str) -> int:
        stack = [-1] #so we don't pop an empty stack when string starts with )
        maxLen = 0
        for idx,c in enumerate(s):
            if c == "(":
                stack.append(idx) #always append (
            else:
                    stack.pop()
                    if len(stack) == 0: #if stack is empty means we can add current bracket which is ) it's the end of invalid string
                        stack.append(idx)
                    else:
                        maxLen = max(maxLen, idx - stack[-1]) #we calculate the max length between current index and the end of invalid element
        return maxLen
    
    def longestValidParentheses(self, s: str) -> int:
        left , right = 0,0
        maxLen = 0
        #scan from left to right
        for c in s:
            if c == "(": #find (, inc left
                left += 1
            else:
                right += 1#find ), inc right
            if left == right: #if equal calc len
                maxLen = max(maxLen, left+right)
            elif right >= left: #if right > left, reset pointers to 0 noting longest string after an invalid string
                left = right = 0
        left , right = 0,0
        for c in reversed(s):
            if c == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxLen = max(maxLen, left+right)
            elif left >= right:#if left > right, reset pointers to 0 noting longest string after an invalid string
                left = right = 0
        return maxLen
                