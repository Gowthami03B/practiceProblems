"""
You work in an automated robot factory. Once robots are assembled, they are sent to the shipping center via a series of autonomous delivery carts, each of which moves packages on a one-way route.

Given input that provides the (directed) steps that each cart takes as pairs, write a function that identifies all the start locations, and a collection of all of the possible ending locations for each start location.

In this diagram, starting locations are at the top and destinations are at the bottom - i.e. the graph is directed exclusively downward.

   A         E      J       Key:  [Origins]
  / \       / \      \             \
 B   C     F   L      M            [Destinations]
  \ /  \  /
   K     G
		/ \
	   H   I 
paths = [
["A", "B"],
["A", "C"],
["B", "K"],
["C", "K"],
["E", "L"],
["F", "G"],
["J", "M"],
["E", "F"],
["G", "H"],
["G", "I"],
["C", "G"]
]

Expected output (unordered):
[ "A": ["K", "H", "I"],
"E:" ["H", "L", "I"],
"J": ["M"] ]
"""
from collections import defaultdict
def findEndlocations(paths):
    graph = defaultdict(list)
    indegree = [0] * 26
    paths = []
    for start, end in paths:
        graph[start].append(end)
        indegree[ord(end) - ord("A")] += 1
    print(graph, indegree)
    queue = deque()
    visited = set()
    for idx,val in enumerate(indegree):
        if val == 0:
            queue.append(chr(ord['A'] - ord(idx)))
            
    while queue:
        start_dest = queue.popleft()
        if indegree[ord(start_dest) - ord("A")] == 0:
            visited.add(start_dest)
        for next_dest in graph[start_dest]:
            indegree[ord(next_dest) - ord("A")] -= 1
            if indegree[ord(next_dest) - ord("A")] == 0:
                queue.append(next_dest)
                res[start_dest].append(next_dest)

def get_path(p):
    graph = defaultdict(list)
    in_degree = [0] * 26
    ms = set()

    for c in p:
        graph[c[0]].append(c[1])
        in_degree[ord(c[1]) - ord("A")] += 1
        ms.add(c[0])
        ms.add(c[1])

    nodes = []
    for i, n in enumerate(in_degree):
        if n == 0 and chr(ord("A") + i) in ms:
            nodes.append(chr(ord("A") + i))
    ans = defaultdict(set)
    
    def _bk(node, tmp):
        if len(graph[node]) == 0:
            ans[tmp[0]].add(node)
            return
        for ngb in graph[node]:
            _bk(ngb, tmp + [node])

    for n in nodes:
        _bk(n, [])
    return ans
paths = [
["A", "B"],
["A", "C"],
["B", "K"],
["C", "K"],
["E", "L"],
["F", "G"],
["J", "M"],
["E", "F"],
["G", "H"],
["G", "I"],
["C", "G"]
]

ans = get_path(paths)
print(ans)
        

# findEndlocations(paths)
