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
        #instead of constructing from top where u need to set the current node's right and modify the tree, why don't you start from bottom?
        #then it becomes post order traversal and you won't disturb the tree when you set the right of current node to prev node
        prev = None
        def dfs(root):
            nonlocal prev
            if root is None:
                return 
            dfs(root.right)#right, left, root
            dfs(root.left) 
            root.right = prev#set right
            root.left = None #set left
            prev = root  #set previous

        dfs(root)
        