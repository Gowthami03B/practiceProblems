# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallestRecursive(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            #at every node we return a list, [left] + [root] + [right]
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        return inorder(root)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorder(root):
            if not root:
                return []
            left = inorder(root.left)
            res.append(root.val)
            right = inorder(root.right)
            return res
        return inorder(root)[k-1]
    
    def kthSmallestIterative(self, root: Optional[TreeNode], k: int) -> int:
        res, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res[k-1]
    
    def kthSmallestDesc(self, root: Optional[TreeNode], k: int) -> int:
        res, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.right
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.left
        print(res)
            