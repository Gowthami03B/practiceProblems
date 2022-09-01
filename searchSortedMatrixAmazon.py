"""
Given an n x n matrix and an integer x, find the position of x in the matrix if it is present. Otherwise, print “Element not found”. 

Every row and column of the matrix is sorted in increasing order. The designed algorithm should have linear time complexity. 

"""
def searchSortedMatrix(nums, x):
    n = len(nums)
    i = 0
    # set indexes for top right element
    j = n - 1
    while ( i < n and j >= 0 ):
     
        if (mat[i][j] == x ):
            return 1
        #since the matrix is sorted, we need to just go lower if curr > x i.e j-1
        if (mat[i][j] > x ):
            j -= 1
        else:#if smaller, go to higher next element, hence i+=1
            i += 1
    return 0

mat = [ [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50] ]
print(searchSortedMatrix(mat, 100))
