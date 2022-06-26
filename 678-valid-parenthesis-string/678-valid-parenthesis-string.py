class Solution:
    def checkValidString(self, s: str) -> bool:
        leftBal, rightBal = 0,0
        for val in s:
            if val in "(*":
                leftBal += 1
            else:
                leftBal -= 1
        
            if leftBal < 0:
                return False
    
        for val in reversed(s):
            if val in ")*":
                rightBal += 1
            else:
                rightBal -= 1
            
            if rightBal < 0:
                return False
        
        return True