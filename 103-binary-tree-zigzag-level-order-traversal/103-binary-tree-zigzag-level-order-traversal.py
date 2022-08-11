# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        if not root:
            return res
        queue = deque([root])
        count = -1
        while queue:
            count += 1
            levels = []
            for _ in range(len(queue)):
                node = queue.popleft()
                levels.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if count%2:
                res.append(levels[::-1])
            else:
                res.append(levels)
        return res
        