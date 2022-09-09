# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBSTRecursive(self, root: Optional[TreeNode]) -> bool:
        #assigning parameters in the declaration itself
        def validate(root: Optional[TreeNode], low = -math.inf, high=math.inf):
            #Empty trees are valid BSTs
            if not root:
                return True
            #if val is not between the low and higher bounds, false
            if root.val <= low or root.val >= high:
                return False
            return (validate(root.left, low, root.val) and validate(root.right,root.val,high))
            
        return validate(root)
    
    def isValidBSTIterative(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [(root,-math.inf,math.inf)]
        while stack:
            root, low, high = stack.pop()
            if not root:
                continue
            if root.val <= low or root.val >= high:
                return False
            stack.append((root.left,-math.inf, root.val))
            stack.append((root.right, root.val,math.inf))
        return True
    
    def isValidBSTInorderRecursive(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)
            
            
        self.prev = -math.inf
        return inorder(root)
    
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack , prev = [], -math.inf
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                if node.val <= prev:
                    return False
                prev = node.val
                root = node.right
        return True
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        def check(root):
            if not root:
                return None

            check(root.left)
            res.append(root.val)
            check(root.right)

        check(root)

        for i in range(1,len(res)):
            if res[i] <= res[i-1]:
                return False

        return True
