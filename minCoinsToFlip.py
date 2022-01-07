# Consider there is a set of coins placed on a board. Some coins are placed in a way that the HEAD will be at the top and some coins are placed in an opposite way (TAIL side at the top). HEAD facing coins can be considered as string "H" and TAIL facing coins can be considered as string "T"

# Example: HTHTTT

# If the coins are arranged in such a manner that all the HEAD facing coins comes first followed by the TAIL facing coins, then the set is called a Beautiful set.

# Beautiful Set : HHHTT

# You need to write a function that takes a string as input and return the minimum number of flips needed to make the coins as a beautiful set.
# https://leetcode.com/discuss/interview-question/1566414/Minimum-flips-for-a-beautiful-set/
class Solution:
    def minflips(self, s):
        Ts = 0
        flips = 0

        for c in s:
            if c == 'T':
                Ts += 1
            else:
                flips = min(flips + 1, Ts)
        return flips

print(Solution().minflips("HTHTTT"))
