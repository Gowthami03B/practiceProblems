class Solution:
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     rows, cols = len(matrix), len(matrix[0])
    #     new = [[0] * cols for _ in range(rows)]
    #     print(new)
    #     for j in reversed(range(cols)):
    #         for i in range(rows):
    #             new[i][j] = matrix[0][i]
    #     print(new)
        
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while(l < r):
            for i in range(r-l):
                top , bottom = l, r
                topLeft = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeft
                print(matrix)
            l += 1
            r -= 1
            
