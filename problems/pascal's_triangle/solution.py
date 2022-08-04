class Solution:
    def generate1(self, numRows: int) -> List[List[int]]:
        res = []
        res.append([1])
        if numRows == 1:
            return res
        #O(numRows^m2)
        while(len(res) < numRows):
            curr = res[-1]
            temp = []
            temp.append(curr[0])
            for i in range(1,len(curr)):
                temp.append(curr[i] + curr[i-1])
            temp.append(curr[-1])
            res.append(temp)
        return res
    
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for rownum in range(numRows):
            row = [None for _ in range(rownum + 1)]
            row[0] = 1
            row[-1] = 1
            for i in range(1,len(row)-1):
                row[i] = res[rownum-1][i-1] + res[rownum-1][i]
            res.append(row)
            
        return res