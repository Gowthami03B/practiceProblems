import re
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def findValidIPV4(queryIP):
            ip_list = queryIP.split(".")
            for num in ip_list:
                if not num.isdigit() or (len(num) >2 and int(num) > 255):
                    return False
                if num[0] == "0" and len(num) > 1:
                    return False
            return True
        
        def findValidIPV6(queryIP):
            ip_list = queryIP.split(":")
            hexdigits = '0123456789abcdefABCDEF'
            for num in ip_list:
                if len(num) == 0 or len(num) > 4 or not all(c in hexdigits for c in num):
                    return False
            return True
        
        if queryIP.count('.') == 3:
            if findValidIPV4(queryIP):
                return "IPv4"
        elif queryIP.count(':') == 7:
             if findValidIPV6(queryIP):
                return "IPv6"
        else:
            return "Neither"
        return "Neither"
            