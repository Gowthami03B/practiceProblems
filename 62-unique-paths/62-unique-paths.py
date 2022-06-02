class Solution:
    def uniquePaths1(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        start = [0,0]
        end = [m-1,n-1]
        queue = deque([start])
        visited = set()
        visited.add((0,0))
        possiblePaths = 0
        while queue:
            r,c = queue.popleft()
            dir = [[0,1],[1,0]]
            if [r,c] == end:
                possiblePaths += 1
                visited.clear()
                queue.clear()
                for dr,dc in dir:
                    originr, originc = start
                    queue.append([originr,originc+1])
                    queue.append([originr+1,originc])
                break
            for dr,dc in dir:
                nr,nc = r,c
                while nr < m and nc < n :
                    nr += dr
                    nc += dc
                    if (nr,nc) not in visited:
                        queue.append([nr,nc])
                        visited.add((nr,nc))
        return possiblePaths
    
    def uniquePathsRecursive(self, m: int, n: int) -> int:
        if m == n == 1:
            return 1
        return self.uniquePaths(m,n-1) + self.uniquePaths(m-1,n)
    
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        
        for row in range(1,m):
            for col in range(1,n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[m-1][n-1]
