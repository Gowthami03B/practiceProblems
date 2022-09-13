class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        if not edges or not edges[0]:
            return -1
        
        graph = defaultdict(list)
        for u,v,weight in edges:
            graph[u].append((v,weight))
            graph[v].append((u,weight))
            
        # print(graph)#adjacency list
        self.minCities ,self.ans = float("inf"),-1#record no of cities, the city which is answer
        
        # The key of this question is: DO NOT mark a city as seen immediately once you reach it, find the minimum distance to this city instead, so that it is possible to use this city to reach another city.
        def bfs(node):
            visited = {node:-1}
            queue= deque([[node,0]])
            while queue:
                curr, d = queue.popleft()
                for nei,dist in graph[curr]:
                        if (nei not in visited or dist + d < visited[nei]) and dist + d <= distanceThreshold:#if nei not in visited then we can check if dist + d <threshold, but if its in visited, then dist+d should be less then visited[nei] else we are taking a wrong longer route
                            queue.append((nei,dist +d))
                            visited[nei] = dist + d 
            total = len(visited)#after bfs is complete
            if total <= self.minCities and node > self.ans:#we need city with higher value and min Cities
                self.minCities,self.ans = total, node
            # print(visited)
        for i in range(n):
            bfs(i)#run bfs for all nodes
         
        return self.ans
    
        """
        6
[[0,3,7],[2,4,1],[0,1,5],[2,3,10],[1,3,6],[1,2,1]]
417
stdout
defaultdict(<class 'list'>, {0: [(3, 7), (1, 5)], 3: [(0, 7), (2, 10), (1, 6)], 2: [(4, 1), (3, 10), (1, 1)], 4: [(2, 1)], 1: [(0, 5), (3, 6), (2, 1)]})
visited
{0: -1, 3: 7, 1: 5, 2: 6, 4: 7}
{1: -1, 0: 5, 3: 6, 2: 1, 4: 2}
{2: -1, 4: 1, 3: 7, 1: 1, 0: 6}
{3: -1, 0: 7, 2: 7, 1: 6, 4: 8}
{4: -1, 2: 1, 3: 8, 1: 2, 0: 7}
{5: -1}
        
        """