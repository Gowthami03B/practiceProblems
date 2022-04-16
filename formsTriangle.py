"""
Given coordinates of three points in a plane P1, P2 and P3, the task is to check if the three points form a triangle or not
Examples: 
 

Input: P1 = (1, 5), P2 = (2, 5), P3 = (4, 6) 
Output: Yes
Input: P1 = (1, 1), P2 = (1, 4), P3 = (1, 5) 
Output: No 

Approach: The key observation in the problem is three points form a triangle only when they don’t lie 
on the straight line, that is an area formed by the triangle of these three points is not equal to zero. 
{Area of Triangle }= {1}{2}*(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))   
"""
def formsTriangle(x1,y1,x2,y2,x3,y3):
    area = (x1 * (y2-y3)) + (x2 * (y3-y1)) +( x3 * (y1-y2))
    if area == 0:
        return 0
    else: 
        return 1

print(formsTriangle(1,5,2,5,4,5))
