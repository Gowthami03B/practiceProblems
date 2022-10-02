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

    def getKth(self, lo: int, hi: int, k: int) -> int:
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