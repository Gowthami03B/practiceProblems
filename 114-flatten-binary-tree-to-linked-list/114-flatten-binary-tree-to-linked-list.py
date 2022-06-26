# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        def dfs(root):# 3, prev 3, 3.right = None
            nonlocal prev
            if root is None:
                return 
            dfs(root.right)
            dfs(root.left) #2 2.right = 3
            root.right = prev
            root.left = None 
            prev = root  #prev = 2

        dfs(root)
        