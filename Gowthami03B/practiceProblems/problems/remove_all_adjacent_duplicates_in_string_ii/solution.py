class Solution:
    def removeDuplicatesBruteForce(self, s: str, k: int) -> str:
        count = 0
        length = -1
        while(length != len(s)):#when length == len(s), no more reductions possible
            length = len(s)
            for i in range(1,len(s)):
                if s[i] == s[i-1]:
                    count += 1
                    if count +1 == k:
                        s = s[:i-k+1] + s[i+1:]#not optimal, making more strings
                        count = 0
                        break#break when we change the string length and start from start
                else:
                    count = 0
        return s

    def removeDuplicatesRecursion(self, s: str, k: int) -> str:
        count = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
                if count +1 == k:
                    s = s[:i-k+1] + s[i+1:]#not optimal, making more strings
                    return self.removeDuplicates(s,k)
            else:
                count = 0
        return s

    def removeDuplicates(self, s, k):
        stack = [['#', 0]] #maintain the character and counts
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
            # print(stack)
        return ''.join(c * k for c, k in stack)