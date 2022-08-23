class Solution:
    def countBinarySubstrings1(self, s: str) -> int:
        res = 0
        prev = 0#prev consecutive values
        tmp = 1 #to keep track of current consecutive 1's or 0's
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                res += min(prev, tmp)#when there's a mismatch, res =min(prev,temp)
                prev = tmp
                tmp = 1
            else:
                tmp += 1
        res += min(prev, tmp)
        return res
    
    def countBinarySubstrings(self, s: str) -> int:
        counts , count,res = [],1,0#same as above but with maintaining counts as separate
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                counts.append(count)
                count = 1
        counts.append(count)
        for i in range(1, len(counts)):
            res += min(counts[i-1],counts[i])
        return res