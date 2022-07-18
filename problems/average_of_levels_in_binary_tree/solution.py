# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels1(self, root: Optional[TreeNode]) -> List[float]:
        if root:
            queue = deque([root])
        res = []
        while queue:
            k, avg = len(queue), 0
            for _ in range(k):
                children = queue.popleft()
                avg += children.val
                if children.left:
                    queue.append(children.left)
                if children.right:
                    queue.append(children.right)
            res.append(avg/k)
        return res
        
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_sum = defaultdict(int)
        level_count = defaultdict(int)
        def dfs(root, level=0):
            if not root:
                return
            level_count[level] += 1
            level_sum[level] += root.val
            dfs(root.left, level +1)
            dfs(root.right, level +1)
        
        dfs(root)
        # print(level_sum, level_count)
        return [level_sum[i]/level_count[i] for i in range(len(level_sum))] 
        
                
        
        
