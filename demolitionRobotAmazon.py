# Demolition Robot
# Given a matrix with values 0 (trenches) , 1 (flat) , and 9 (obstacle) you have to find minimum distance to reach 9 (obstacle). If not possible then return -1.
# The demolition robot must start at the top left corner of the matrix, which is always flat, and can move on block up, down, right, left.
# The demolition robot cannot enter 0 trenches and cannot leave the matrix.
# Sample Input :
# [1, 0, 0],
# [1, 0, 0],
# [1, 9, 1]]
# Sample Output :
# 3
# This question can be solved by using BFS or DFS.
def demolitionRobot(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxrow, maxcol = rows - 1, cols - 1
        visit = set()
        dir = [
            (-1,0),(0,-1),(0,1),(1,0)]
        
        if grid[0][0] != 1:
            return -1
        queue = deque()
        queue.append((0,0))
        visit.add((0,0))
        grid[0][0] = 1
        while queue:
            r,c = queue.popleft()
            dist = grid[r][c]
            # if grid[r][c] == 9:
            #     return dist
            for dr,dc in dir:
                nr, nc = r + dr, c + dc
                if(0 <= nr <= maxrow and 0 <= nc <= maxcol):
                    if grid[nr][nc] == 9:
                        return dist
                    if(grid[nr][nc] == 1 and (nr,nc) not in visit):
                        queue.append((nr, nc))
                        grid[nr][nc] = dist + 1
                visit.add((nr,nc))
        return -1
