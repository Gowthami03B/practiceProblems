from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '*':
                    queue.append([i,j,0])
        while queue:
            row, col, steps = queue.popleft()
            if (row,col) in visited:
                continue
            else:
                visited.add((row,col))
                
            if grid[row][col] == "#":
                return steps
        
            if row > 0 and (row-1,col) not in visited and grid[row-1][col] != "X":
                queue.append([row-1,col,steps+1])
            if row < rows -1 and (row+1,col) not in visited and grid[row+1][col] != "X":
                queue.append([row+1,col,steps+1])
            if col > 0 and (row,col-1) not in visited and grid[row][col-1] != "X":
                queue.append([row,col-1,steps+1])
            if col < cols-1 and (row,col+1) not in visited and grid[row][col+1] != "X":
                queue.append([row,col+1,steps+1])
        return -1