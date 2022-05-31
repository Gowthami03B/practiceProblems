# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if p is None or q is None:#if p or q is None, return False before recursion
        #         return False
        return self.dfs(p,q)  
    
    def dfs(self,p: Optional[TreeNode], q: Optional[TreeNode]):
            if p is None and q is None:
                return True
            elif p is None and q is not None: #either one is None, false
                return False
            elif q is None and p is not None:
                return False
            if p.val != q.val: #if values don't match false
                return False
            return self.dfs(p.left, q.left) and self.dfs(p.right, q.right) #need to combine the results from left and right, each returns a bool value
