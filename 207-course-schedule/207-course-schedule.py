from collections import deque
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        for course,prereq in prerequisites:
            graph[prereq].append(course) #graph to adjacency list
            indegree[course] += 1 #a course which is only in prerequisite list and not in course list has indegree 0
        print(graph, indegree)
        queue = deque() #queue
        count = 0 #keep note of explored courses
        visited = set()
        for i in range(len(indegree)):
            if indegree[i] == 0 and i not in visited: #if indegree is 0 and not visited
                queue.append(i)
            
            while(queue):
                course = queue.popleft()
                if course in visited:
                    return
                if indegree[course] == 0:#if indegree is 0, we can complete the course, hence inc count and add to visited
                    count += 1
                    visited.add(course)
                    for course in graph[course]: #for each dependent course 
                            indegree[course] -= 1 #decrement indegree of dependent courses as we completed their prerequiste course
                            if indegree[course] == 0:#if indegree is 0, we need to complete the course, hence add to queue
                                queue.append(course)
                    
        return numCourses == count
        