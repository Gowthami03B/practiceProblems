# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    res.append(int(path))
                else:
                    dfs(root.left, path)
                    dfs(root.right, path)
        dfs(root, "")
        return sum(res)