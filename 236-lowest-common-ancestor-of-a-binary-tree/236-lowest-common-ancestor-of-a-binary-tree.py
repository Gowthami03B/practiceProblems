# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
brute force -
say 6,5
- traverse from root to p - store path in set - [3,5,6]
- traverse from root to q - [3,5]
last common one is the least common ancestor

say 0,8
- traverse from root to 0, will take us through - [3,5,6,2,7,4,1,0,8],we will also have all these nodes

Optimal Solution -
- travel from p to parent instead
- set Parent for nodes
- traverse through parents and mark as visited
- traverse from q to parent, first node in visited is the lowest common
"""

class Solution:
    def __init__(self):
        self.visited = set()
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.setParent(root)
        while p is not None:
            self.visited.add(p.val)
            p = p.parent
        while q is not None:
            if q.val in self.visited:
                return q
            q = q.parent
        return None
    
    def setParent(self, root, par=None):
        if root is None:
            return
        root.parent = par
        self.setParent(root.left, root)
        self.setParent(root.right, root)
    
        