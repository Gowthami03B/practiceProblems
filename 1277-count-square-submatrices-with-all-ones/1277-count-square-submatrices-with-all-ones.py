class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        Take an example of this matrix:

        0 1 1 1
        1 1 1 1
        0 1 1 1
        Maintain a running counter of length of each 2x2 square, and store the length of the square on the bottom right corner of each of those squares.

        Starting at cell (1, 1), get length of the square -> min(value at (0,1), value at (1,0), value at (0,0)) + 1 = 1
        As you navigate through the rest of the matrix, the matrix becomes:

        0 1 1 1
        1 1 2 2
        0 1 2 3
        
        """
        if not matrix or len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i > 0 and j > 0:
                        matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j - 1]) + 1#min of up,diagonal,left values
                    res += matrix[i][j]#count the 1's squares until now
        return res