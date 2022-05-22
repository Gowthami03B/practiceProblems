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
        # if p.val == root.val or q.val == root.val and not self.ancestor:
        #      self.ancestor = root
        # if (p.val <= root.val <= q.val or q.val <= root.val <= p.val) and not self.ancestor:
        #     self.ancestor = root
        if (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left,p,q)
        elif (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
