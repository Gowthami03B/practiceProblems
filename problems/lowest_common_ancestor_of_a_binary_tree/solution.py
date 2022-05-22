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

Optimal Solution when p,q are treenodes-
- travel from p to parent instead
- set Parent for nodes
- traverse through parents and mark as visited
- traverse from q to parent, first node in visited is the lowest common

if p,q are values instead of treenodes
- need to find if p and q exist in tree
- if so, find the lowest common ancestor
"""

class Solution:
    def __init__(self):
        self.visited = set()
        self.ancestor = None
    def lowestCommonAncestorParentPointer(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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
        
    def dfs(self,root):
        if root is None or self.ancestor:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        total = left + right + (root in self.targets)
        if total == 2 and not self.ancestor:
            self.ancestor = root
        return total
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.targets = [p,q]
        self.dfs(root)
        return self.ancestor
        
    
        