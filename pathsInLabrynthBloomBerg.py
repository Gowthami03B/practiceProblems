"""
A labyrinth of zeros and ones is given. Zero - "cannot pass", One - "can pass."
List all paths from top left to bottom-right corner. You can move only down or to the right.
Input: 2-dimensional array that contains the labyrinth.
Example:
Input = [[1,0,1], [1,1,1], [0,1,1]]
Input in 2D:
1 0 1
1 1 1
0 1 1

Output:
(0,0) (1,0) (1,1) (2,1) (2,2)
(0,0) (1,0) (1,1) (1,2) (2,2)
"""
def pathsInLabrynth(grid):
    paths = []
    dir = [[1,0],[0,1]]
    rows = len(grid)
    cols = len(grid[0])
    def backtrack(i,j,path):
        if (i,j) == (rows-1,cols-1):
            paths.append(list(path))
            return

        for nr,nc in dir:
            dr,dc = i+nr, j+nc
            if 0<= dr < rows and 0<=dc < cols and grid[dr][dc] != 0:
                path.append((dr,dc))
                backtrack(dr, dc, path)
                path.pop()

    backtrack(0,0, [(0,0)])
    return paths if len(paths) > 0 else "No Paths"

grid = Input = [[1,0,1], [1,1,1], [0,1,1]]
print(pathsInLabrynth(grid))
