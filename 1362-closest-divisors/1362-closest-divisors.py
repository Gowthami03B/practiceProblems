import math
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        if num == 1:
            return [1,2]
        res1 = self.findDivisor(num + 1)
        res2 = self.findDivisor(num + 2)
        # print(res1)
        # print(res2)
        if len(res1) > 0 and len(res2) > 0:
            if(res1[0] - res1[1] < res2[0] - res2[1]):
                return res1
            else:
                return res2
        elif len(res1) > 0:
            return res1
        else:
            return res2
        
    def findDivisor(self, num : int):
        diff = float('inf')
        res = []
        for i in range(2, int(math.sqrt(num)) + 1):
            if(num % i == 0):
                temp = int(num / i) - (i)
                print(temp)
                if(temp < diff):
                    diff = temp
                    res.clear()
                    res.append(int(num / i))
                    res.append(i)
                print(res)
        return res
                
        