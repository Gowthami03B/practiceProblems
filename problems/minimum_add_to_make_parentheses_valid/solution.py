class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        window = {')' : '('}
        stack = []
        for c in s:
            if c in window:
                if stack:
                    topElement = stack.pop()
                    if(window[c] == topElement):
                        continue
                    else:
                        stack.append(topElement)
                        stack.append(c)
                if not stack:
                    stack.append(c)
            else:
                stack.append(c)
        return len(stack)