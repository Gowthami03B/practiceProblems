# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = collections.deque([root])
        while(queue):
            res1 = []
            for _ in range(len(queue)):
                child = queue.popleft()
                if child.left:
                    queue.append(child.left)
                if child.right:
                    queue.append(child.right)
                print(child.val)
                res1.append(child.val)
            res.append(res1)
        return res