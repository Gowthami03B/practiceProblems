import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        window = {}
        for i in range(len(points)):
            dist = math.sqrt(pow(points[i][0],2) + pow(points[i][1],2))
            window[i] = dist
        sortedL = sorted(window, key = window.get)
        res = []
        for i in range(k):
            res.append(points[sortedL[i]])
        return res
