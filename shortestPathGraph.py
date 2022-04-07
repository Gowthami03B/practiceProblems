# Given an (unweighted) graph, return the length of the shortest path between two nodes A and B.

# Input:

# graph: {
#   0: [1, 2],
#   1: [0, 2, 3],
#   2: [0, 1],
#   3: [1]
# }
# A: 0
# B: 3

from collections import deque
from typing import List
def shortest_path(graph : List[List[int]], a : int, b : int) -> int:
    def get_neighbours(node):
        return graph[node]

    #to find levels, neighbours added at once are at the same level, hence we need the for loop on len(queue)
    def bfs(root, target):
        queue = deque([root])
        visited = set([root])
        level = 0
        while len(queue) > 0:
            n = len(queue)
            for n in range(n):
                node = queue.popleft()
                if node == target:
                    return level
                for neighbour in get_neighbours(node):
                    if neighbour in visited:
                        continue
                    queue.append(neighbour)
                    visited.add(neighbour)
            level += 1 #should be outside for loop to count neighbours level 
    
    #tree traversal works without for loop at level(queue)
    # def bfs(start, target):
    #     queue = deque([start])
    #     visited = set([start])
    #     level = 0
    #     while len(queue) > 0:
    #         node = queue.popleft()
    #         if node == target:
    #             return level
    #         for neighbour in get_neighbours(node):
    #             if neighbour in visited:
    #                 continue
    #             queue.append(neighbour)
    #             visited.add(neighbour)
    #         level += 1
    return bfs(a, b)

res = shortest_path([[1, 2],
[0, 2, 3],
[0, 1],
[1]], 0, 3)
print(res)
