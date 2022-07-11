class Solution:
    def mySqrt(self, x: int) -> int:
        #since we only have to return the integer part, and since the square root is < x/2, we only search in that space, find a number and see if n*n < x or > x 
        if x == 0 or x == 1:
            return x
        start , end = 1, x//2
        while(start <= end):
            mid = (start + end)//2
            if mid*mid > x:
                end = mid - 1
            elif mid*mid < x:
                start = mid + 1
            else:
                return mid
        return end
            