class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(matrix)):
            for j in range(1,len(matrix[0])):
                matrix[i][j] += matrix[i][j-1]
        print(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        totSum = 0
        if col1:
            for row in range(row1,row2+1):
                totSum += self.matrix[row][col2] - self.matrix[row][col1 - 1]
        else:
            for row in range(row1,row2+1):
                totSum += self.matrix[row][col2]
        return totSum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)