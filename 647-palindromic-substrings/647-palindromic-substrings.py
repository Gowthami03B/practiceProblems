class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        count = 0
        for i in range(n):
            for j in range(i,n):
                count += self.isPalindrome(s,i,j)
        return count
                    
    def isPalindrome(self,s,i,j):
        if i == j :
            return 1
        while(i < j):
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return 0
        return 1
                