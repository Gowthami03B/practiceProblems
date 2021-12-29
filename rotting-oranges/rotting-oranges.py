import collections
from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows , cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        print(grid)
        def access(r,c):
            if(r < 0 or r ==rows or c < 0 or c == cols or (r,c) in visit or grid[r][c] == 0):
                return
            q.append([r,c])
            visit.add((r,c))
            
        freshoranges = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i,j])
                    visit.add((i,j))
                elif grid[i][j] == 1:
                    freshoranges+= 1
        
        if freshoranges == 0:
            return 0
        countMin = -1
        
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                access(r+1,c)
                access(r,c + 1)
                access(r-1,c)
                access(r,c - 1)
                if grid[r][c] == 1:
                    freshoranges-= 1
                grid[r][c] = 2
            countMin+=1
        print(grid)
        return countMin if freshoranges == 0 else -1
