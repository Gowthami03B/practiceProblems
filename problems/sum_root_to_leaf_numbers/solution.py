# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers1(self, root: Optional[TreeNode]) -> int:
        #bad approach - string concatenation and conversion to int
        # res = []
        # def dfs(root, path):
        #     if root:
        #         path += str(root.val)
        #         if not root.left and not root.right:
        #             res.append(int(path))
        #         else:
        #             dfs(root.left, path)
        #             dfs(root.right, path)
        # dfs(root, "")
        # return sum(res)
    
        #good approach
        res = 0
        def dfs(root, curr):
            nonlocal res
            if root:
                curr = curr*10 + root.val
                if not root.left and not root.right:
                    res += curr
                else:
                    dfs(root.left, curr)
                    dfs(root.right, curr)
        dfs(root, 0)
        return res
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sumTotal = 0
        stack = [(root,0)]
        while(stack):
            root, curr = stack.pop()
            if root:
                curr = curr*10 + root.val
                if not root.left and not root.right:
                    sumTotal += curr
                else:
                    stack.append((root.right, curr))
                    stack.append((root.left, curr))
        return sumTotal