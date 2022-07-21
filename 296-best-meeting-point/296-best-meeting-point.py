class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        x_coords, y_coords = [],[]
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    x_coords.append(i)
                    y_coords.append(j)
                
        x_coords.sort()
        y_coords.sort()
        mid_x = x_coords[len(x_coords)//2]
        mid_y = y_coords[len(y_coords)//2]
        return sum([abs(mid_x - x_coord) for x_coord in x_coords]) + sum([abs(mid_y - y_coord) for y_coord in y_coords])