# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees2(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        stack = [(root1,root2)]
        while stack:
            r1, r2 = stack.pop()
            if r2 is None:
                continue#if r2 is None, then don't need to do anything
            r1.val += r2.val
            if r1.left is None:
                r1.left = r2.left #if r1 is not there, then r1 = r2
            else:
                stack.append((r1.left, r2.left)) #if both values exist, add to stack
            
            if r1.right is None:
                r1.right = r2.right
            else:
                stack.append((r1.right, r2.right))
        return root1
                
    def mergeTrees1(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        We can traverse both the given trees in a preorder fashion. At every step, we check if the current node exists(isn't null) for both the trees. If so, we add the values in the current nodes of both the trees and update the value in the current node of the first tree to reflect this sum obtained.
        """
        if root1 is None:#If at any step, one of these children happens to be null, we return the child of the other tree to be added as a child subtree to the calling parent node
            return root2 
        if root2 is None:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
    
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
            if not root1:
                return root2
            elif not root2:
                return root1
            else:
                root1.val += root2.val
                root1.left = self.mergeTrees(root1.left, root2.left)	
                root1.right = self.mergeTrees(root1.right, root2.right)	
            return root1

            
            