from collections import defaultdict
from collections import deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        for emp, mgr in enumerate(manager):
            if mgr != -1:
                graph[mgr].append(emp)
        print(graph)
        def dfs(head, cur, maxtime):
            if not graph[head]:
                return max(maxtime, cur)
            for emp in graph[head]:
                maxtime = dfs(emp, cur+informTime[head], maxtime)
            return maxtime
        return dfs(headID, 0, 0)
    
    
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
    