class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:
        #using BFS will make us find all rooms at distance 1 and distance+1 and so on
        #search from gates instead of rooms
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        dir = [[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append([i,j])#add all gates to queue
        while(queue):#start BFS from all gates simultaneously
            r,c = queue.popleft()
            for dr,dc in dir:
                nr,nc = r+dr, c+dc
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] > grid[r][c] + 1:#if curr dist is > nearest dist from gate, update dist
                    grid[nr][nc] = grid[r][c] + 1#+1 from nearest gate
                    queue.append([nr,nc])
