class Solution:
    def uniquePathsRecursive(self, m: int, n: int) -> int:
        if m == n == 1:
            return 1
        return self.uniquePaths(m,n-1) + self.uniquePaths(m-1,n)
    
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)] #create a dp array
        #we already populated our base case, first row and col
        #to reach 0,2 from 0,1 , it takes one step, hence all first row and col, 1step
        for row in range(1,m): #for each inner row
            for col in range(1,n): #for each inner col
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[m-1][n-1]
