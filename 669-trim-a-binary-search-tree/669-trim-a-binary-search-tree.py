# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim(node):
            if not node:
                return None
	#post order traversal
            left = trim(node.left) #go left
            right = trim(node.right) #go right
            if low <= node.val <= high: #if the root is within bounds, then return the node as is by appending left and right
                node.left = left
                node.right = right
                return node
            return left if left else right#if the root is not within bounds,we need to ignore the root and return it’s children to the calling node
 
        return trim(root)
    
    def trimBST2(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim(node):
            if not node:
                return None
            elif node.val > high: #if node.val > high, then it’s right is higher than high and we need not go to these branches, we go left
                return trim(node.left)#As per BST, if a node.val < low, then it’s left side is lesser than low, we go right
 
            elif node.val < low:
                return trim(node.right)
            else: #if node is in bounds, we go left and right and return node
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
 
        return trim(root)
