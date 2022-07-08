class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        #[[1,0],[2,0],[3,1],[3,2]]
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course) #we maintain map from prereq : courses dependent on it, so above example becomes 0 : 1,2; 1 : 3, 2 : 3
            indegree[course] += 1 #we also maintain an array that stores information of how to complete course at index, how many courses need to be finished, hence
          #  [0, 1, 1, 2]; to complete 1,2 , we need to do 0 and to complete 3, we need to do 1,2
        print(graph, indegree)
        queue = deque()
        visited = []
        for idx, prereq_count in enumerate(indegree):
            if prereq_count == 0:
                queue.append(idx)#start from the course that can be completed first
                
        while queue:
            course = queue.popleft()
            if indegree[course] == 0:#if indegree is 0, we can complete the course, hence add to visited
                visited.append(course)
            for prereq in graph[course]:#for every course dependent on this, we can decrement their indegree as they are no longer dependent on this one
                indegree[prereq] -= 1
                if indegree[prereq] == 0:#if indegree is 0, we can complete the course, hence add to queue
                    queue.append(prereq)
        return visited if len(visited) == numCourses else []
                        
                    