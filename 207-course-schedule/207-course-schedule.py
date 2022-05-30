from collections import deque
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        for course,prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        print(graph, indegree)
        queue = deque()
        count = 0
        visited = set()
        for i in range(len(indegree)):
            if indegree[i] == 0 and i not in visited:
                queue.append(i)
            
            while(queue):
                course = queue.popleft()
                if course in visited:
                    return
                if indegree[course] == 0:
                    count += 1
                    visited.add(course)
                    for course in graph[course]:
                        # if course in graph:
                            indegree[course] -= 1
                            if indegree[course] == 0:
                                queue.append(course)
                    
        return numCourses == count
#         def topsort(prereq, coursePre=None):
#             if prereq in visited:
#                 return
#             if prereq in graph:
#                 topsort(graph[prereq])
#             visited.add(prereq)
#             courseOrder.append(prereq)
            
#         for prerequisite in graph.keys():
#             topsort(prerequisite)
        