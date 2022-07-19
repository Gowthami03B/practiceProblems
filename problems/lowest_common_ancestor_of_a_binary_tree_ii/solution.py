# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ancestor = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.targets = [p.val, q.val]#this works when p and q are just values
        self.dfs(root,p,q)
        return self.ancestor if self.ancestor else None
    
    def dfs(self, root: 'TreeNode', p,q):
        if root is None or self.ancestor:
            return 0
        left = self.dfs(root.left,p,q)
        right = self.dfs(root.right,p,q)
        total = left + right + (root.val in  self.targets)
        if total == 2 and not self.ancestor:
            self.ancestor = root
        return total