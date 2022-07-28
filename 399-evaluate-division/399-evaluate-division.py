class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def backtrack_evaluate(curr_node, target_node, acc_product, visited):
            visited.add(curr_node)
            ret = -1.0
            neighbors = graph[curr_node]#say target is b, neighbours = graph[a], i.e {b:value}
            if target_node in neighbors:
                ret = acc_product * neighbors[target_node]#so neighbours is graph[a][target=b] gives the value
            else:#say source =a, target = c [["a","b"],["b","c"]]
                for neighbor, value in neighbors.items():#neighbours =graph[a]= {b:value}
                    if neighbor in visited:
                        continue
                    ret = backtrack_evaluate(
                        neighbor, target_node, acc_product * value, visited)
                    if ret != -1.0:#that means we find our value and can break ur loops
                        break
            visited.remove(curr_node)#so that we can freshly evaluate next expressions, for backtracking
            return ret
        
        """
        We could reformulate the equations with the graph data structure, where each variable can be represented as a node in the graph, and the division relationship between variables can be modeled as edge with direction and weight.
        
        Let NN be the number of input equations and MM be the number of queries.
Time Complexity: O(M⋅N), O(N)- to build graph, then O(M.N) - to traverse the graph for each query
        """
        graph = defaultdict(defaultdict)
        #for ["a","b"],["b","a"] = {'a': defaultdict(None, {'b': 1.5}), 'b': defaultdict(None, {'a': 0.66666666666666
        for (dividend, divisor),value in zip(equations,values):
            graph[dividend][divisor] = value #graph[a] has value as a default dict
            #level_one = {'level_two': { 'level_three': {'some_key': 'some_value' }}}, to access final value - level_one['level_two']['level_three']['some_key']
            #similarly graph[a][b] = value
            graph[divisor][dividend] = 1 / value
            
        res = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:#when either of these are not present in graph
                ret = -1.0
            elif dividend == divisor:#if both are same
                ret = 1.0
            else:
                visited = set()
                ret = backtrack_evaluate(dividend, divisor, 1,visited)
            res.append(ret)
        return res