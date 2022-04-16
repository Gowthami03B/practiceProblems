"""
Given three corner points of a triangle, and one more point P. Write a function to check whether P lies within the triangle or not.
For example, consider the following program, the function should return true for P(10, 15) and false for P'(30, 15) 

              B(10,30)
                / \
               /   \
              /     \
             /   P   \      P'
            /         \
     A(0,0) ----------- C(20,0) 
Solution: 
Let the coordinates of three corners be (x1, y1), (x2, y2) and (x3, y3). And coordinates of the given point P be (x, y)
1) Calculate area of the given triangle, i.e., area of the triangle ABC in the above diagram. Area A = [ x1(y2 – y3) + x2(y3 – y1) + x3(y1-y2)]/2 
2) Calculate area of the triangle PAB. We can use the same formula for this. Let this area be A1. 
3) Calculate area of the triangle PBC. Let this area be A2. 
4) Calculate area of the triangle PAC. Let this area be A3. 
5) If P lies inside the triangle, then A1 + A2 + A3 must be equal to A. 
O(1),O(1)
"""
def isInside(x1, y1, x2, y2, x3, y3, x4,y4):
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x1, y1, x2, y2,x4,y4)
    A2 = area(x1, y1, x3, y3,x4,y4)
    A3 = area(x2, y2, x3, y3,x4,y4)
    if A1+A2+A3 == A:
        return 1
    else:
        return 0

def area(x1, y1, x2, y2, x3, y3):
 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)

print(isInside(0, 0, 20, 0, 10, 30, 10, 15))
