# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = collections.defaultdict(list)
        def findHeight(root):
            if not root:
                return 0, None
            left, val = findHeight(root.left)
            right, val = findHeight(root.right)
            res[1+max(left,right)].append(root.val)
            return ([1+max(left,right), root.val])
        
        findHeight(root)
        return list(res.values())
            
            