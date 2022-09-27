class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        res = []
        '''
        Let us start from a graph with only two nodes. As one can imagine, there is only one single path to connect the only two nodes in the graph. if we add another node, we have 2 paths.one insight is that every time we add a new node into the graph, the number of paths would double(2^N). Max 2^N−1 −1 number of paths between the starting and the ending nodes. O(N) to build the path by traversing all the nodes atmost, hence O(2^N. N)
        '''
        def backtrack(node, path):
            if node == target:
                res.append(list(path))
                return
            
            for neighbour in graph[node]:
                path.append(neighbour)
                backtrack(neighbour,path)
                path.pop()
            
        path = [0]
        backtrack(0,path)
        return res