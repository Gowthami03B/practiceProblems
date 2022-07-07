class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        #check if slopes are equal between all the points to see if they lie in straight line
        #y = mx + b, m = x1-x2/y1-y2
        #check if slope m1 = m2, x1-x2/y1-y2 == x2-x3/y2-y3
        (x1,y1),(x2,y2) = coordinates[0], coordinates[1]
        # for i in range(2, len(coordinates)):    
        #     x3,y3 = coordinates[i]
        #     if (x1-x2)*(y2-y3) != (y1-y2)*(x2-x3):
        #         return False
        # return True
        
        return all((x1-x2)*(y2-y3) == (y1-y2)*(x2-x3) for x3,y3 in coordinates)