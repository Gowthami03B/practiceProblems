class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        reverse = 0
        while(x):
            reminder = x % 10
            x = x//10
            reverse = reverse* 10 + reminder
        return reverse == temp
        