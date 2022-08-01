class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visited = set()
        freshOranges = 0
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                    visited.add((i,j))
                elif grid[i][j] == 1:
                    freshOranges += 1#keep track of fresh oranges
                    
        while(queue):
                        r,c,minElapsed = queue.popleft()
                        for dr,dc in dir:
                            nr = r + dr
                            nc = c + dc
                            if 0<= nr < rows and 0<= nc < cols and (nr,nc) not in visited and grid[nr][nc] == 1:
                                grid[nr][nc] = 2
                                freshOranges -= 1#deduct freshOranges
                                if freshOranges == 0:
                                    return minElapsed + 1
                                queue.append((nr,nc,minElapsed+1))#minElapsed + 1 for next iteration
                                visited.add((nr,nc))
        return 0 if freshOranges == 0 else -1#if there are no fresh oranges to be rotten, then 0 else -1
            