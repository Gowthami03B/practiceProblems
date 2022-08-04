from collections import deque
class Solution:
    def numIslands1(self, grid: List[List[str]]) -> int:
        def bfs(i,j):
            queue = deque()
            queue.append([i,j]) #multiple values, []
            visited.add((i,j))
            while queue:
                r,c = queue.popleft()
                dir = [[1,0],[0,1],[-1,0],[0,-1]]
                for dr, dc in dir:
                    nr, nc = r+dr, c+dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1" and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append([nr,nc])
        countIslands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(i,j)
                    countIslands += 1
        return countIslands
    
    def numIslands(self, grid: List[List[str]]) -> int:
        countIslands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in visited:
                    queue.append([i,j]) #multiple values, []
                    visited.add((i,j))
                    while queue:
                        r,c = queue.popleft()
                        dir = [[1,0],[0,1],[-1,0],[0,-1]]
                        for dr, dc in dir:
                            nr, nc = r+dr, c+dc
                            if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1" and (nr,nc) not in visited:
                                visited.add((nr,nc))
                                queue.append([nr,nc])
                    countIslands += 1
        return countIslands
        
        
