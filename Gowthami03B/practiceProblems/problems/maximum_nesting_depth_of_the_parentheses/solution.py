class Solution:
    def maxDepth(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        depth = 0
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if stack:
                    depth=max(depth,len(stack))
                    stack.pop()
        return depth