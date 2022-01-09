class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxrow, maxcol = rows - 1, cols - 1
        dir = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        if grid[0][0] != 0 or grid[maxrow][maxcol] !=0:
            return -1
        queue = deque()
        queue.append((0,0))
        grid[0][0] = 1
        while queue:
            r,c = queue.popleft()
            dist = grid[r][c]
            if (r,c) == (maxrow,maxcol):
                return dist
            for dr,dc in dir:
                nr, nc = r + dr, c + dc
                if(0 <= nr <= maxrow and 0 <= nc <= maxcol and grid[nr][nc] == 0):
                        queue.append((nr, nc))
                        grid[nr][nc] = dist + 1
        return -1