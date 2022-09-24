
class Solution:
    def decodeString1(self, s: str) -> str:
        stack = []
        temp_string = []
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
    
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                temp_string = []
                k = []
                while stack and stack[-1] != '[':
                    temp_string.append(stack.pop())
                # print(temp_string)
                if stack[-1] == '[':
                    stack.pop()#pop open bracket
                while stack and stack[-1].isdigit():
                    k.append(stack.pop())#pop digit
                temp_string.reverse()
                k.reverse()
                k = int("".join(k))
                temp_string *= k
                # print(temp_string)
                for c in temp_string:
                    stack.append(c)

        return "".join(stack)