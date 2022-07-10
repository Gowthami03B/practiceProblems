class Solution:
    #convert to string
    def reverse1(self, x: int) -> int:
        if x == 0:
            return 0
        elif x > 0:
            reversed_int = int(str(x)[::-1])
            if -2**31 <= reversed_int <= 2**31 - 1:
                return reversed_int
            else:
                return 0
        else:
            reversed_int = -int(str(-x)[::-1])
            if -2**31 <= reversed_int <= 2**31 - 1:
                return reversed_int
            else:
                return 0
            
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        neg = False
        if x < 0:
            neg = True
        x = abs(x)
        reversed_int = 0
        while x > 0:
            reminder = x % 10
            x = x//10
            reversed_int = reversed_int * 10 + reminder
        if neg:
            if -2**31 <= -reversed_int <= 2**31 - 1:
                return -reversed_int
            else:
                return 0
        else:
            if -2**31 <= reversed_int <= 2**31 - 1:
                return reversed_int
            else:
                return 0
            
            
            