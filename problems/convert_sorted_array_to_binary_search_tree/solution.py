# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #always picks left middle as root
    #example start 0, end 3, mid is 1 [0,1,2,3], but since it's even, mid could also have been 2, but we pick 1
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums) - 1
        def helper(start,end):
            if start > end:
                return None
            mid = start + (end-start)//2
            root = TreeNode(nums[mid])
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            return root
        return helper(0,n)
        
    #always picks right middle as root
    #example start 0, end 3, mid is 1 [0,1,2,3], but since sum of left and right is odd == even no of elements, mid should be 2 - right middle
    def sortedArrayToBST1(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums) - 1
        def helper(start,end):
            if start > end:
                return None
            mid = start + (end-start)//2
            if (start + end) %2:#if no of elements between start and end are even, pick right middle i.e mid + 1
                mid +=1
            root = TreeNode(nums[mid])
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            return root
        return helper(0,n)