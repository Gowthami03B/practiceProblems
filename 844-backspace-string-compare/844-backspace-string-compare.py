class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s , stack_t = [],[]
        for i in range(len(s)):
            if s[i] != '#':
                stack_s.append(s[i])
            elif stack_s:
                stack_s.pop()
        for i in range(len(t)):
            if t[i] != '#':
                stack_t.append(t[i])
            elif stack_t:
                stack_t.pop()
        
        return "".join(stack_s) == "".join(stack_t)
        
        