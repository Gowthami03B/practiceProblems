"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.created_nodes = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.created_nodes:
            return self.created_nodes[node]
        
        cloned_node = Node(node.val,[])
        self.created_nodes[node]= cloned_node
        
        if node.neighbors:
            cloned_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return cloned_node
            