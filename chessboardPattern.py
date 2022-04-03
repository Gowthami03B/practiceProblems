def chessboardPattern(num):
	# Write your code here
    #Write a function that prints a chessboard pattern, with 'W' being white square and 'B' being black. Input is an integer that is the number of squares on the board. Output is a 2D char array. For example,
# input:
# 2
# Output:
# W B
# B W
# The topmost left square is always 'W'.
#heart of the problem is knowing that the diagonal values are the same

    #Method 1
    result = [[None for i in range(num)] for j in range(num)]
    #Method 2
    result1 = [[None for i in range(num)] for j in range(num)]

    for i in range(num):
        for j in range(num):
            if(i == 0):
                if(j%2 == 0):
                    result[i][j] = 'W'
                else:
                    result[i][j] = 'B'
            else:
                temp = abs(j-1)
                result[i][j] = result[i-1][temp]
    print(result)
    for i in range(num*num):
	    m,n = divmod(i, num) #generates m,n starting from 0,0 until the end of the grid
	    if (m+n)%2: #very clever again to see the pattern if m + n % 2== 0 , it's always W
		    result1[m][n] = 'B'
	    else:
		    result1[m][n] = 'W'	
    return result1

print(chessboardPattern(4))
