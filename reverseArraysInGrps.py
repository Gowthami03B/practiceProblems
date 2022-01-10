from itertools import chain
class Solution:
    def reverseArrays(self, data: list[int], opr : list[list[int]]):
        for x,y  in opr:
            temp = data[x:y+1]
            k = list(chain(data[:x], list(reversed(temp)), data[y+1:]))
            data = k
        return data

data = [5,3,1,2,3]
opr = [[0,1], [1,3]]
print(Solution().reverseArrays(data, opr))
