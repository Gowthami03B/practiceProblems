class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0 #if no islands, then will return this which is 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = collections.deque([])
        for i in range(rows):
            for j in range(cols):
                #for every island or 1 found, do a BFS in all directions
                #but you are gonna visit all islands only once since you check visited hence O(M*N) for time and space
                if grid[i][j] == 1 and (i,j) not in visited:
                    islands = 1
                    queue.append([i,j])
                    visited.add((i,j))
                    while(queue):
                        r,c = queue.popleft()
                        dir = [[0,1],[1,0],[-1,0],[0,-1]]
                        for dr,dc in dir:
                            nr,nc = r + dr,c + dc
                            #For each direction, if another island is found, add to queue and increment island count
                            if (0 <= nr <= rows - 1) and (0 <= nc <= cols-1) and grid[nr][nc] and (nr,nc) not in visited:
                                islands += 1
                                queue.append([nr,nc])
                                visited.add((nr,nc))
                    maxArea = max(maxArea, islands)#when queue is empty, means finished traversing that island, find maxArea
        return maxArea
