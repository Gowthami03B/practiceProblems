class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        # build a graph in form of an adjacency list
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1]) #even though graph[edge[0]] is not present, default dict will not throw an error and creates it
            graph[edge[1]].append(edge[0]) #bidirectional graph

        # add the the source to the BFS queue
        queue = deque([source])
        seen = set()
        while queue:
            node = queue.popleft()
            seen.add(node)
            for n in graph[node]:
                if n not in seen:
                    if n == destination:
                        return True
                    queue.append(n)
        return False