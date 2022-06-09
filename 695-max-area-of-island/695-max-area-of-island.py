class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = collections.deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    islands = 1
                    queue.append([i,j])
                    visited.add((i,j))
                    while(queue):
                        r,c = queue.popleft()
                        dir = [[0,1],[1,0],[-1,0],[0,-1]]
                        for dr,dc in dir:
                            nr,nc = r + dr,c + dc
                            if (0 <= nr <= rows - 1) and (0 <= nc <= cols-1) and grid[nr][nc] and (nr,nc) not in visited:
                                islands += 1
                                queue.append([nr,nc])
                                visited.add((nr,nc))
                    maxArea = max(maxArea, islands)
        return maxArea
