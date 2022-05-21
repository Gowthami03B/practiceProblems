class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack, res = [], []
        leftDir = 0
        for num in asteroids:
            if num > 0:
                stack.append(num)
            elif num < 0 and len(stack) == 0:
                res.append(num)
                continue
            elif num < 0:
                self.checkStack(stack,num,res)
        return res + stack
        
        
    def checkStack(self,stack, num,res):
            if len(stack) > 0:
                lastEle = stack.pop()
                if lastEle < abs(num):
                    self.checkStack(stack,num,res)  
                elif abs(num) < lastEle:
                    stack.append(lastEle) 
                elif abs(num) == lastEle:
                    return
            else:
                res.append(num)
                    
                    
                