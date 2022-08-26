class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        strng = list(s)
        count_map = defaultdict(int)
        for i in strng:
            count_map[i] +=1
        odd = 0
        result = 0
        left = 0
        right = len(strng)-1
        # If we found more then one odd number
        for freq in count_map.values():
            if freq % 2 != 0:
                odd += 1
        if odd > 1: return -1
        
        while left < right:
            l = left
            r = right
            while strng[l] != strng[r]:#compare start and end
                r -= 1#find r where char are same
            if l == r:#we found the odd element, swap adjacent move towards middle
                strng[r],strng[r+1] = strng[r+1],strng[r]
                result += 1
                continue
            else:
                # Normal element  move towards right of string
                while r < right:
                    strng[r],strng[r+1] = strng[r+1],strng[r]
                    r += 1
                    result += 1
            left += 1
            right -= 1
        return result