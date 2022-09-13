class Solution:
    def validTree1(self, n: int, edges: List[List[int]]) -> bool:
        #build adjacency list
        #“a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
        # A graph with n nodes has n-1 edges
        # there cannot be a cycle, if there's a cycle, then no of edges != n-1
        #undirected graph, hence 0-1 and 1-0
        #a graph should be fully connected, means no unconnected nodes
        edgemap = collections.defaultdict(list)
        for u,v in edges:
            edgemap[u].append(v)
            edgemap[v].append(u)
        visited = set() #contains the set of visited nodes
        queue = collections.deque([[0]])
        while queue:
            for _ in range(len(queue)):
                children = queue.popleft()
                for child in children:
                    if child not in visited:
                        queue.append(edgemap[child])
                        visited.add(child)
        return True if len(visited) == n and len(edges) == n - 1 else False
    
    def validTree2(self, n: int, edges: List[List[int]]) -> bool:
        #intuition is to do DFS, we need to compare parents, if the parent is not same as child when child in visited, that means the node has 2 different origins
        if len(edges) != n-1:
            return False
        g = defaultdict(list)
        visit = [0]*n
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        visited = {}
        def dfs(node, parent):
            visited[node] = parent
            
            for nei in g[node]:
                if nei in visited:
                    if parent and nei != parent:
                        return False
                else:
                    if not dfs(nei, node):
                        return False
            return True
            
            
        if not dfs(0, None):
            return False
        return len(visited) == len(g)
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        g = defaultdict(list)
        visit = [0]*n
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for child in g[node]:
                if child not in visited:
                    dfs(child)
        
        dfs(0)
        return len(visited) == n