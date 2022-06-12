class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        dir = [[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append([i,j])
        while(queue):
            r,c = queue.popleft()
            for dr,dc in dir:
                nr,nc = r+dr, c+dc
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] > grid[r][c] + 1:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append([nr,nc])
