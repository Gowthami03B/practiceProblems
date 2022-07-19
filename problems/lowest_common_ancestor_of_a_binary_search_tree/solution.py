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
        if root is None:
            return
        if (p.val < root.val and q.val < root.val):#if both less than root, then continue on left side
            return self.lowestCommonAncestor(root.left,p,q)
        elif (p.val > root.val and q.val > root.val):#else right side
            return self.lowestCommonAncestor(root.right,p,q)#else root is the commo
        else:
            return root
