class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
#         #by creating adjacency lists in dict to store edges
#         #O(N+E), O(N)
#         graph = defaultdict(list)
#         for edge in edges:
#             graph[edge[0]].append(graph[edge[1]])
#             graph[edge[1]].append(graph[edge[0]])
        
#         for key, value in graph.items():
#             if len(value) == len(edges):
#                 return key
#         return -1
        
#         #using array to count no of edges to each node
#         #O(N+E), O(N)
#         degree = [0 for i in range(len(edges) + 2)]
#         for a,b in edges:
#             degree[a] += 1
#             degree[b] += 1
#         for i in range(1, len(degree)):
#             if degree[i] == len(edges):
#                 return i
#         return -1
        
        #since we know that edges always represents a valid star graph, we can just check which is common and elimiate time and space complexity - constant time and space
        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]
        return -1