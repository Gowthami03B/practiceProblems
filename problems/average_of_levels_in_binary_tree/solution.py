# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
            res = []
            if root:
                queue = deque([root])
            while queue:
                sum, k = 0,len(queue)
                for _ in range(k):
                    node = queue.popleft()
                    sum += node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                res.append(sum/k)
            return res

    
        
                
        
        
