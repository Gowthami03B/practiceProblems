# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #example [5,4,8,11,null,13,4,7,2,null,null,null,1], 22

        if not root:
            return False
        targetSum -= root.val #subtract from targetSum at each node
        if not root.left and not root.right: #if it's a leaf node, return True iftargetSum is 0
            return targetSum == 0 #once we reach 7, targetSum is -5 and we return false here but at 11(it's parent), target sum is 2 which will be passed down to right subtree
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum) #else recursively navigate left and right subtree