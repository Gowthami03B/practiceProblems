# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    """
    Similar to binary search, however, we need to cut the rectangle into 4 parts as shown in the figure below.
If the quarter area return as false, which means no ship in this area, we can safely return 0
if the quarter area returns as True, we should keep on dividing that area into four parts to further explore.
The base case will be the top and bottom points are the same, then we can get the exact result. It is if True, we have one ship, if False, we have zero ship.
One subtle thing is in order to have no overlap for these four parts, we need to add a center point by 1 as shown in the figure.
    """
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def d_c(bottom, top):
            if bottom.x>top.x or bottom.y>top.y:return 0 #when bottom > top
            if (top.x, top.y)  == (bottom.x, bottom.y):     
                return int(sea.hasShips(top, bottom)) #when same ask hasShip
            else:
                if not sea.hasShips(top, bottom):return 0#when top and bottom are different, see if they have ship
                bot_x, bot_y = bottom.x, bottom.y
                top_x, top_y = top.x, top.y
                center_x, center_y = (bot_x+top_x)//2, (bot_y+top_y)//2
                #check the picture or draw quadrants to understand context
                #basically 2 points with (x,y)
                f1 = d_c(bottom, Point(center_x, center_y))
                f2 = d_c(Point(center_x+1, center_y+1), top)
                f3 = d_c(Point(bot_x, center_y+1), Point(center_x, top_y))
                f4 = d_c(Point(center_x+1, bot_y), Point(top_x, center_y))
                return f1+f2+f3+f4
        return d_c(bottomLeft, topRight)    
        