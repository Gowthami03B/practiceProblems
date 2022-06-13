# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
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
    
    #level order traversal with stack
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack, res = [(root,0)], collections.defaultdict(list)
        while stack:
            root , height = stack.pop()
            if root:
                if root.right:
                    stack.append((root.right, height + 1))
                if root.left:
                    stack.append((root.left, height + 1))
                res[height].append(root.val)
        return list(res.values())