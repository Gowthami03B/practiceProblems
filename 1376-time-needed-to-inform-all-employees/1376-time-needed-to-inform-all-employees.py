from collections import deque
class Solution:
    def numOfMinutesTest(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        for emp, mgr in enumerate(manager):
            if mgr != -1:
                graph[mgr].append(emp) #build adjacency list
        print(graph)
        def dfs(head, cur, maxtime):
            if not graph[head]:
                return max(maxtime, cur)
            for emp in graph[head]:
                maxtime = dfs(emp, cur+informTime[head], maxtime)
            return maxtime
        return dfs(headID, 0, 0) #start with head
    
    
#         if len(manager) == 0 or (len(manager) == 1 and manager[0] == -1):
#             return 0
#         #head of company is only employee
#         companyGraph = defaultdict(list)
#         for idx, val in enumerate(manager,0):
#             if val == -1:
#                 continue
#             if val == headID:
#                 companyGraph[headID].append(idx)
#             else:
#                 companyGraph[val].append(idx)
#         print(companyGraph)
#         return self.informTimes(companyGraph, headID, informTime)
        
#     def informTimes(self,companyGraph,headID,informTime):
#         queue = deque([companyGraph[headID]])
#         # sumTime= 0
#         sumTime = informTime[headID]
#         while(queue):
#             tempTime, k = 0,len(queue)
#             for _ in range(k):
#                 node = queue.popleft()
#                 print(node)
#                 for n in node:
#                     if n in companyGraph:
#                         queue.append(companyGraph[n])
#                         tempTime = max(informTime[n],tempTime)
#                         print(tempTime)      
#             sumTime += tempTime
#         return sumTime if sumTime !=0 else informTime[headID]
    def numOfMinutes(self, n, headID, manager, informTime):
        
        graph = collections.defaultdict(list)
        for emp, mgr in enumerate(manager):
            if mgr != -1:
                graph[mgr].append(emp) #build adjacency list
        print(graph)

        # bfs 
        queue = collections.deque()
        queue.append((headID, 0)) #mgr, time taken to inform manager
        totTime = 0

        #for each emp, store the emp and time that was needed to inform that emp
        while queue:
            for i in range(len(queue)):
                currmgr, currtime = queue.popleft()
                totTime = max(totTime, currtime)
                for emp in graph[currmgr]: 
                    queue.append((emp, informTime[currmgr] + currtime))
        return totTime