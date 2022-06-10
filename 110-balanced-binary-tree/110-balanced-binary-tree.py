# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]
    
    def dfs(self,root):
            if not root:
                return True, -1
            isleftBalanced, left = self.dfs(root.left)
            if not isleftBalanced:
                return False, 0
            isrightBalanced, right = self.dfs(root.right)
            if not isrightBalanced:
                return False, 0
            return (abs(left - right) < 2), 1 + max(left, right)