class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        #since we can have 0 zeros and 0 ones for it to be increasing
        ones =flips =0
        for c in s:
            if c == '1':
                ones += 1
            else:
                flips += 1
                
            flips =min(flips,ones)#min of both these counts is the no of flips needed
        return flips