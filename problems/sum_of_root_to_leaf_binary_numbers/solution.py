# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeafRecursive(self, root: Optional[TreeNode]) -> int:
        #same problem as Sum Root to Leaf Numbers, but in binary, instead of 10, multiply by 2
        #100 - 2^2, 2^1, 2^0 - last one is multiplied by 2^2, just like 10^2
        res = 0
        def sumBinary(root, curr):
            nonlocal res
            if root:
                curr = curr*2 + root.val
                if not root.left and not root.right:
                    res += curr
                else:
                    sumBinary(root.left, curr)
                    sumBinary(root.right, curr)
        
        sumBinary(root, 0)
        return res

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        sumTotal = 0
        stack = [(root,0)]
        while(stack):
            root, curr = stack.pop()
            if root:
                curr = curr*2 + root.val#calculate running sum
                print(root.val,curr)
                if not root.left and not root.right:
                    sumTotal += curr
                else:
                    stack.append((root.right, curr))
                    stack.append((root.left, curr))
        return sumTotal

