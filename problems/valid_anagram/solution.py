class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # #2 constant arrays
        # s_arr = [0] * 26
        # t_arr = [0] * 26
        # for c in s:
        #     s_arr[ord('a')-ord(c)] += 1
        # for c in t:
        #     t_arr[ord('a')-ord(c)] += 1
        # if s_arr != t_arr:
        #     return False
        # return True
    
        #1 constant arrays
        s_arr = [0] * 26
        for c in s:
            s_arr[ord('a')-ord(c)] += 1
        for c in t:
            s_arr[ord('a')-ord(c)] -= 1
        for count in s_arr:
            if count >0 or count < 0:
                return False
        return True