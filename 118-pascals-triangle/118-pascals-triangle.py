class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        res.append([1])
        if numRows == 1:
            return res
        # res.append([1,1])
        # if numRows == 2:
        #     return res
        while(len(res) < numRows):
            curr = res[-1]
            temp = []
            temp.append(curr[0])
            for i in range(1,len(curr)):
                temp.append(curr[i] + curr[i-1])
            temp.append(curr[-1])
            res.append(temp)
        return res
                