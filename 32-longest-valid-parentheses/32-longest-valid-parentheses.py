class Solution:
    def longestValidParenthesesStack(self, s: str) -> int:
        stack = []
        maxLen = 0
        for idx,c in enumerate(s):
            if c == "(":
                stack.append(idx)
            else:
                if len(stack) > 0:
                    stack.pop()
                    if len(stack) == 0:
                        stack.append(idx)
                    else:
                        maxLen = max(maxLen, idx - stack[-1])
        return maxLen
    
    def longestValidParentheses(self, s: str) -> int:
        left , right = 0,0
        maxLen = 0
        for c in s:
            if c == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxLen = max(maxLen, left+right)
            elif right >= left:
                left = right = 0
        left , right = 0,0
        for c in reversed(s):
            if c == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxLen = max(maxLen, left+right)
            elif left >= right:
                left = right = 0
        return maxLen
                