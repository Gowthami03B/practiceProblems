class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1: #if the no of edges are < n-1, then there won't be enough cables to connect the unconnected
            return -1
        
        def dfs(node):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        
        graph = defaultdict(set)
        for u,v in connections:#adjacency list
            graph[u].add(v)
            graph[v].add(u)
            
        connected_components = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i) # 0: 1,2,3 , all of these are visited and are connected hence increment connected_components, #4,5 new edges and unconnected, hence also increment them
                connected_components += 1
        return connected_components - 1 #The logic for how many edges you need to connect each component is the same as before: n - 1. If connected components is 1 and no other edges, then 0 edges are needed, if 2, i.e 2 components are individually connected hence connect both with 1 edge, if 3 then 2 is needed, and so on. So, just return the number_of_connectected_components - 1 as your final answer.
            
        