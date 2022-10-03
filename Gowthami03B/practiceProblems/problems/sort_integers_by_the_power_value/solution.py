class Solution:
    def getKth1(self, lo: int, hi: int, k: int) -> int:
        arr = []
        for i in range(lo,hi+1):
            arr.append(i)
        def getPower(num):
            queue = collections.deque()
            queue.append((num,0))
            while queue:
                curr,steps = queue.popleft()
                if curr == 1:
                    return steps
                nextnode = curr//2 if not curr%2 else (curr*3)+1
                queue.append((nextnode, steps+1)) 

        arr.sort(key=getPower)
        return arr[k-1]

    def getKth2(self, lo: int, hi: int, k: int) -> int:
        res = []
        for i in range(lo , hi+1):
            ans = i
            steps = 0
            while ans != 1:
                ans = ans//2 if not ans%2 else (ans*3)+1
                steps += 1
            res.append((steps,i))
        res.sort()
        return res[k-1][1]

    def getKth3(self, lo: int, hi: int, k: int) -> int:
        
        dic = {}
        res = {}
        def powerValue(num,dic):
            if num == 1:
                return 0
            
            if num in dic:
                return dic[num]
            
            if num % 2:#odd number
                dic[num] = 1 + powerValue(3*num+1,dic)
                return dic[num]
            else:
                dic[num] = 1 + powerValue(num//2,dic)
                return dic[num]
            
        for i in range(lo,hi+1):
            res[i] = powerValue(i,dic)
        print(res)
        return sorted(res.items(),key = lambda x:x[1])[k-1][0]

    def getKth(self, lo: int, hi: int, k: int) -> int:
        #from 12 to get to 1 == 1 + (12//2 (half)) to get to 1
        # dic:{2: 1, 4: 2, 8: 3, 16: 4, 5: 5, 10: 6, 3: 7, 6: 8, 12: 9, 20: 7, 40: 8, 13: 9, 26: 10, 52: 11, 17: 12, 34: 13, 11: 14, 22: 15, 7: 16, 14: 17} 2 -> 1 1 step, 4 -> 1 , 2 steps
        dp = collections.defaultdict(int)#stores for all intermediary values
        dic = collections.defaultdict(int) #stores for the values we want
        def getPower(num,dp):
            if num == 1:
                return 0
            if num in dp:#if exists return value
                return dp[num]
            if num % 2:#odd number
                dp[num] = 1 + getPower((num*3)+1,dp)
                return dp[num]
            else:
                dp[num] = 1 + getPower(num//2,dp)
                return dp[num]

        for i in range(lo,hi+1):
            dic[i] = getPower(i,dp)
        return sorted(dic.items(),key=lambda x:x[1])[k-1][0]