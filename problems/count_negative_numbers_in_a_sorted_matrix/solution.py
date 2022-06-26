class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if grid and grid[0][0] < 0:
            return m*n
        
        cnt = 0
        for row in grid:
            startIndex = self.search(row)
            cnt += len(row) - startIndex
        return cnt
    
    def search(self,grid):
        left, right = 0, len(grid)
        while(left < right):
            mid = (left+right)//2
            if grid[mid] >= 0:
                left = mid + 1
            else:
                right = mid
        return left
    
    
    
    