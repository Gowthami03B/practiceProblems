# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
    
        # def maxTree(nums):
            maxNum = max(nums)
            index = nums.index(maxNum)
            root = TreeNode(maxNum)
            if len(nums[:index]) > 0:
                root.left = self.constructMaximumBinaryTree(nums[:index])
            if len(nums[index+1:]) > 0:
                root.right = self.constructMaximumBinaryTree(nums[index+1:])
            return root
    