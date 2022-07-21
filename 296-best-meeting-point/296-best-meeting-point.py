class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        #in 1d, meeting point between points is the mid point
        #1-1-0-0-1-1, 5/2 = 2, i.e first 0
        #1-1-0-0-1
        #hence we collect the xcoor, ycoord
        x_coords, y_coords = [],[]
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    x_coords.append(i)
                    y_coords.append(j)
                
        x_coords.sort()#sort them
        y_coords.sort()
        mid_x = x_coords[len(x_coords)//2]#find the mid value of x and y
        mid_y = y_coords[len(y_coords)//2]
        #sum of distances from start to mid for both x and y list
        return sum([abs(mid_x - x_coord) for x_coord in x_coords]) + sum([abs(mid_y - y_coord) for y_coord in y_coords])