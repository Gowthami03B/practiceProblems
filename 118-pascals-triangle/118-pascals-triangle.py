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
    
    #O(numRows^2) since outer loop takes O(numRows), inner loop runs for prev row's no of elements times, so 1+2+3...
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for rownum in range(numRows):#for each no in numRows
            row = [None for _ in range(rownum + 1)]#no of elements to rownum + 1
            row[0] = 1#first and last are always 1
            row[-1] = 1
            for i in range(1,len(row)-1):#loop thru rest of row
                row[i] = res[rownum-1][i-1] + res[rownum-1][i]#prev rows i + prev row's i-1
            res.append(row)
            
        return res