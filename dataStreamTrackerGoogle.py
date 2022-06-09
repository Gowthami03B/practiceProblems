"""
https://leetcode.com/company/google/discuss/1992719/google-or-Tech-Screen-or-SDE-1
"""

import math
class Tracker:

    def __init__(self):
        self.track = {}
        self.mostTrackedEle = 0
        self.mostTrackedCnt = 0
        self.sum = 0
        self.count = 0
        self.maxVal = -math.inf
        self.minVal = math.inf

    def trackNum(self, num: int) -> None:
        if num in self.track:
            self.track[num] += 1
            if self.track[num] > self.mostTrackedCnt:
                self.mostTrackedEle = num
                self.mostTrackedCnt = self.track[num]
        else:
            self.track[num] = 1
        self.sum += num
        self.count += 1
        self.maxVal = max(self.maxVal, num)
        self.minVal = min(self.minVal, num)
    def findAvg(self) -> int:
        return self.sum / self.count
    
    def findMode(self) -> int:
        return self.mostTrackedEle

    def findMax(self) -> int:
        return self.maxVal

    def findMin(self) -> int:
        return self.minVal

obj = Tracker()
obj.trackNum(1)
obj.trackNum(1)
obj.trackNum(1)
obj.trackNum(1)
obj.trackNum(1)
obj.trackNum(10)
obj.trackNum(10)
obj.trackNum(2)
obj.trackNum(3)
obj.trackNum(9)
param_2 = obj.findMax()
param_3 = obj.findMin()
param_4 = obj.findAvg()
param_5 = obj.findMode()
print(param_2,param_3,param_4,param_5)
