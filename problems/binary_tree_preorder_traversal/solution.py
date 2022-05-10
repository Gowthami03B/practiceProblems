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
    
        res,stack = [],[root]
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return res