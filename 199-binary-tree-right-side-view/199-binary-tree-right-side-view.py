# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        queue = collections.deque([(root)])
        res = []
        while queue:
            k = len(queue)
            while k > 0:
                k -= 1
                node = queue.popleft()
                if k == 0:
                    res.append(node.val)
                if node.left:
                    queue.append((node.left))
                if node.right:
                    queue.append((node.right))
        return res