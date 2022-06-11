# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # def dfs(root: Optional[TreeNode]):
        #     if root:
        #         res.append(root.val)
        #         dfs(root.left)
        #         dfs(root.right)
        #     return res
        # return dfs(root)
    
        if not root:
            return []
        stack , res = [],[]
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                root = node.right
        return res