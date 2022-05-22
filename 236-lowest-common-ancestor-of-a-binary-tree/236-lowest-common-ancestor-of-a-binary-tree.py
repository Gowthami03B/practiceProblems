# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.setParent(root)
        visited = set()
        while p:
            visited.add(p.val)
            p = p.parent

        while q is not None:
            if q.val in visited:
                return q
            q = q.parent
    
    def setParent(self, root, par=None):
        if root is None:
            return
        root.parent = par
        self.setParent(root.left, root)
        self.setParent(root.right, root)
    
        