# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        queue = collections.deque([(root)])
        res = []
        while queue:
            k = len(queue)
            while k > 0:#intuition - the nodes are the nodes that are seen last at each level
                k -= 1#dec k
                node = queue.popleft()
                if k == 0:#when k is 0 for each level, that's the last node
                    res.append(node.val)
                if node.left:
                    queue.append((node.left))
                if node.right:
                    queue.append((node.right))
        return res
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def helper(node, level):
            if node is None:
                return
            if len(res) == level:#since we visit right node, the node we visit first in each level from right side is the right view node, hence we check if level == len(res), append to res
                res.append(node.val)
            helper(node.right, level + 1)#we visit right node first
            helper(node.left, level + 1)
        helper(root, 0)
        return res