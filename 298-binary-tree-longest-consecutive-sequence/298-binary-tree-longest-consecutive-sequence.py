# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(root,parent,currlen):
            if root is None:
                return 0
            if parent and root.val == parent.val + 1:
                currlen += 1
            else:
                currlen = 1
            return max(currlen, dfs(root.left,root,currlen), dfs(root.right,root,currlen))
        return dfs(root,None,0)
        