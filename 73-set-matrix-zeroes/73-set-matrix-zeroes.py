class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        isCol = False #to set 1st col to 0's when True
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            if matrix[i][0] == 0:#check if first col needs to be set to 0's
                isCol = True
            for j in range(1,cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1,rows):
            for j in range(1,cols):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
                    
        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0
        if isCol:
            for i in range(rows):
                matrix[i][0] = 0
        
        
    def setZeroesWithSpace(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        rowsSet = set()
        colsSet = set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowsSet.add(i)
                    colsSet.add(j)
        
        for i in range(rows):
            for j in range(cols):
                if i in rowsSet or j in colsSet:
                    matrix[i][j] = 0