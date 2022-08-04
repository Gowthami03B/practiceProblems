"""
There are N distinct integers arranged on a circle. The distance between any two adjacent numbers is 1. The task is to travel on this circle starting with the smallest number, then moving to the second smallest, third smallest, and so on until the largest number and print the minimum travel distance.
Examples: 

Input: arr[] = {3, 6, 5, 1, 2, 4} 
Output: 8 
1 -> 2 (Left to right) 
2 -> 3 (Left to right) 
3 -> 4 (Right to left) 
4 -> 5 (Left to right or right to left) 
5 -> 6 (Right to left)
"""
def circularArrayPaths(nums):
    n = len(nums)
    val = [None] * n
    for i in range(n):
        val[i] = (nums[i],i)#store indices and arr val
    val.sort()
    mindist =0 
    print(val)
    for i in range(1,n):#mindist between 2 values, is diff between their indices (say clockwise) or n - diff between their indices in anti clockwise
        mindist += min(abs(val[i][1] - val[i-1][1]), n- abs(val[i][1] - val[i-1][1]))
    return mindist
nums  = [3,6,5,1,2,4]
print(circularArrayPaths(nums))
