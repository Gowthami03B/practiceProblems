class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        parenthesis_map = {"}": "{", "]":"[",")":"("}#map closing to open
        stack = []
        for c in s:
            if c in parenthesis_map:#for all closing brackets
                topEle = stack.pop() if stack else '#'#get top element if stack else return a dummy element so we can return False even if one pairing doesn't match
                if parenthesis_map[c] != topEle:#if mapping doesn't exist in map
                    return False
            else:
                stack.append(c)#for all opening brackets
        return True if not stack else False
                    