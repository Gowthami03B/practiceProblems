
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        repeat_string= ""
        final_string=""
        k = ""
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                while stack and stack[-1] != '[':
                    repeat_string += stack.pop()
                print(repeat_string)
                if stack[-1] == '[':
                    stack.pop()#pop open bracket
                while stack and stack[-1].isdigit():
                    k += stack.pop()#pop digit
                k = int(k[::-1])
                for _ in range(k):
                    final_string += repeat_string
                    
                for j in reversed(range(len(final_string))):
                    stack.append(final_string[j])
                repeat_string= ""
                final_string=""
                k = ""
        return "".join(stack)