class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
#         graph = defaultdict(list)
#         for edge in edges:
#             graph[edge[0]].append(graph[edge[1]])
#             graph[edge[1]].append(graph[edge[0]])
        
#         for key, value in graph.items():
#             if len(value) == len(edges):
#                 return key
#         return -1
    
        degree = [0 for i in range(len(edges) + 2)]
        for a,b in edges:
            degree[a] += 1
            degree[b] += 1
        for i in range(1, len(degree)):
            if degree[i] == len(edges):
                return i
        return -1