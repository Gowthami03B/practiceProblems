class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #build adjacency list
        #“a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
        # all nodes must have atleast 1 indegree except root
        # there cannot be a cycle
        edgemap = collections.defaultdict(list)
        indegree = [0] * n
        for u,v in edges:
            edgemap[u].append(v)
            edgemap[v].append(u)
            # indegree[v] += 1
        print(edgemap,indegree)
        # if indegree.count(0) > 1:
        #     return False
        visited = set()
        queue = collections.deque([[0]])
        while queue:
            for _ in range(len(queue)):
                children = queue.popleft()
                for child in children:
                    if child not in visited:
                        queue.append(edgemap[child])
                        visited.add(child)
        return True if len(visited) == n and len(edges) == n - 1 else False