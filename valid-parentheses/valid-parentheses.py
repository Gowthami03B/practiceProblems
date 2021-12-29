class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        window = {'}' : '{', ']' : '[',')' : '('}
        for c in s:
            if c in window:
                topElement = stack.pop() if stack else '#'
                if window[c] != topElement:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True