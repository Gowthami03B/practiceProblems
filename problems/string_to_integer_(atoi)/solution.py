import re
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(' ')
        sign = 1
        if len(s) == 0:
            return 0
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        res = re.match("[0-9]+",s)
        if not res:
            return 0
        num = int(res.group(0))
        MAX_LIMIT = pow(2,31)
        if(num >= MAX_LIMIT):
            if sign == 1:
                return MAX_LIMIT - 1
            else:
                return -MAX_LIMIT
        return num * sign