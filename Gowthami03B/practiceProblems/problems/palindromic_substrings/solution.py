class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
#         if n == 0:
#             return 0
        count = 0
#         for i in range(n):
#             for j in range(i,n):
#                 count += self.isPalindrome(s,i,j)
#         return count
                    
#     def isPalindrome(self,s,i,j):
#         print('check is palindrome')
#         if i == j :
#             return 1
#         while(i < j):
#             if s[i] == s[j]:
#                 i += 1
#                 j -= 1
#             else:
#                 return 0
#         return 1
#         dp = [[False] * n for _ in range(n)]        
#         # print(dp)
#         for i in range(n):
#             dp[i][i] = True
#             count += 1
        
#         for i in range(n-1):
#             if s[i] == s[i+1]:
#                 dp[i][i+1] = True
#                 count += 1
#             else:
#                 dp[i][i+1] = False
#         # print(count, dp)    
#         for i in reversed(range(n-1)):
#             for j in range(i+1,n):
#                 if s[i] == s[j]:
#                     dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
#                     if dp[i][j]:
#                         # print(dp[i][j])
#                         count += 1
#                 else:
#                     dp[i][j] = False
#         print(dp)
#         return count
        #we consider that every character is the center of a palindrome
        for i in range(n):
            #odd-length palindromes, single character center
            count += self.expandCenter(s,i,i)
            #even-length palindromes, consecutive characters center
            count += self.expandCenter(s,i,i+1)
            
        return count
    
    def expandCenter(self, s, start, end):
            print(start,end)
            count = 0
            while(start >= 0 and end < len(s)):
                if s[start] != s[end]:#the first and last characters don't match!
                    break
                start -= 1#go left
                end += 1#expand right
                count += 1#increment count
            return count
                