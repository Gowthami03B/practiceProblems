class Solution:
    """
    1- There are more open parenthesis but we have enough '*' so we can balance the parenthesis with ')'
2- There are more close parenthesis but we have enough '*' so we can balance the parenthesis with '('
3- There are as many '(' than ')' so all parenthesis are balanced, we can ignore the extra '*'
    """
    def checkValidString1(self, s: str) -> bool:
        leftBal, rightBal = 0,0
        #left to right and check count of all (*
        #here we consider * as open bracket
        #if leftBal goes neg then brackets are not equal
        for val in s:
            if val in "(*":
                leftBal += 1
            else:
                leftBal -= 1
        
            if leftBal < 0:
                return False
    
        #right to left and check count of all )*
        #here we consider * as close bracket
        #if rightBal goes neg then brackets are not equal
        for val in reversed(s):
            if val in ")*":
                rightBal += 1
            else:
                rightBal -= 1
            
            if rightBal < 0:
                return False
        
        return True #if both bal is 0 or left == right then opencnt == closecnt and TRUE
    
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0