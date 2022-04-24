# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    #recursion
    def invertTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        else:
            invertleft = self.invertTree(root.left)
            invertright = self.invertTree(root.right)
            root.left = invertright
            root.right = invertleft
            return root
    
    #iterative - add to queue, pop, invert, add subtrees and loop while queue
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        queue = deque([root])
        while(queue):
            current = queue.popleft()
            current.left,current.right = current.right,current.left
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root