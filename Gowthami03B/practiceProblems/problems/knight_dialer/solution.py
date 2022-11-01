class Solution:
    def knightDialer1(self, n: int) -> int:#memoization recursion
        d = [(4,6),(6,8),(7,9),(4,8),(3,9,0),(),(1,7,0),(2,6),(1,3),(2,4)]       # Create a graph, index is the vertex and values are the edges
        cache = {}
        
        def dfs(i, n):
            if n == 0: return 1
            elif (i, n) not in cache:# Memoization
                cache[i, n] = sum(dfs(val, n-1) for val in d[i])
                
                if i in [1,4,7]: 
                    cache[i+2, n] = cache[i, n] # Symmetry
                elif i in [3,6,9]: 
                    cache[i-2, n] =cache[i, n]
            print(cache)
            return cache[i, n]

        return sum(dfs(i, n-1) for i in range(10)) % ((10**9+7))
    
    #bottom up DP
    def knightDialerBottomUp(self, n: int) -> int:
        transitions = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        dp = [[0 for _ in range(10)] for _ in range(n)]
        
        # base case
        for i in range(10):
            dp[-1][i] = 1
        
        for i in range(n-2, -1, -1):
            for d in range(10):
                for reach_d in transitions[d]:
                    dp[i][d] = (dp[i][d] + dp[i+1][reach_d]) % (10**9+7)
        
        ans = 0
        for s in dp[0]:
            ans = (ans + s) % (10**9+7)
        return ans
    
    #https://alexgolec.dev/google-interview-questions-deconstructed-the-knights-dialer/
    def knightDialer(self, N: int) -> int:
        pad, cnt = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]], [1]*10
        #initially we have 10 numbers hence cnt is initialized to 10
        for _ in range(N-1):
            next_cnt = [1]*10#temp array
            for i in range(10):#for 10 numbers
                next_cnt[i] = sum(cnt[j] for j in pad[i]) % (10**9+7)#for each number we can reach from i in pad[i], we get the no of numbers we can go to [2, 2, 2, 2, 3, 0, 3, 2, 2, 2] == from 0, u can reach 2 numbers 4,6 hence 2, from 4 we can reach [0,3,9] hence 3 etc
#[6, 5, 4, 5, 6, 0, 6, 5, 4, 5] == 2nd level, from 4 we can reach 3 and from 6 we can reach another 3, hence from 0, to dial a number of size 2, we can dial 6 unique numbers

            # print(next_cnt)
            cnt = next_cnt#next_cnt becomes cnt for next level
        return sum(cnt) % (10**9+7)