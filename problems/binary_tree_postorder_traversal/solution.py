# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # def dfs(root: Optional[TreeNode]):
        #     if root:
        #         dfs(root.left)
        #         dfs(root.right)
        #         res.append(root.val)
        #     return res
        # return dfs(root)
    
        res , stack = [],[root]
        while stack:
            root = stack.pop()
            if root:
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)
                res.insert(0,root.val) #insert root first ie at the end, 0th position keeps on overwritten
                # order -[ left(inserted 3rd), right(inserted 2nd), root(inserted 1st)]
        return res
                