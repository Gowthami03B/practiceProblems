class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if(len(trust) < n - 1):
            return -1
        indegree = [0 for i in range(n+1)] #maintain 2 lists
        outdegree = [0 for i in range(n+1)]
        for a,b in trust:
            indegree[b] += 1 #a trusts b, hence indegree of b is incremented and outdegree of a is incremented 
            outdegree[a] += 1
        for i in range(1,n+1):
            if indegree[i] == n-1 and outdegree[i] == 0: #townjudge has no outdegree, and n-1 indegree
                return i
        return -1
            