class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(graph[edge[1]])
            graph[edge[1]].append(graph[edge[0]])
        
        for key, value in graph.items():
            if len(value) == len(edges):
                return key
        return -1