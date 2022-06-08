class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connected = 0
        graph = collections.defaultdict(list)
        visited = set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node):
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)
        
        #start dfs
        for i in range(n):
            if i not in visited:#if a node is not in visited
                connected += 1 #increment connected and perform dfs on graph[node]
                visited.add(i)
                dfs(i)
                
        return connected
    
    def countComponentsIterative(self, n: int, edges: List[List[int]]) -> int:
        #4, [[0,1],[0,2],[1,2]]; here 0-1-2 are connected and 3 is another node
        connected = 0
        graph = collections.defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for i in range(n):
            if i not in graph:
                graph[i] = []
        #0,1
        #1,0,2
        #2,1
        #3,4
        #4,3
        queue = deque([[0]])
        visited = set()
        while(queue):
            for _ in range(len(queue)):
                neighbours = queue.popleft()
                for neighbour in neighbours:
                    if neighbour not in visited:
                        queue.append(graph[neighbour])
                        visited.add(neighbour)
            if not queue:#queue is empty, means one connected component traversal is coomplete, we check for other nodes and append to queue
                connected += 1
                for node in graph.keys():
                    if node not in visited:
                        queue.append([node])
                        break
        return connected