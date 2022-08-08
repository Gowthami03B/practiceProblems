# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        res = [root.val]
        left_boundary = self.findleft(root.left)
        right_boundary = self.findright(root.right)
        leaves=[]
        if root.left or root.right:
            self.findLeaves(root,leaves)
        res += left_boundary + leaves + right_boundary
        return res
        
    def isleaf(self,root):
        return not root.left and not root.right
    
    def findleft(self,root):
        node,parent = root,root
        res = []
        while node and not self.isleaf(node):
            res.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right
        # print(res)
        return res
    
    def findright(self,root):
        node,parent = root,root
        res = []
        while node and not self.isleaf(node):
            res.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
        # print(res)
        return res[::-1]
    
    def findLeaves(self,root,res):
        if root and self.isleaf(root):
            res.append(root.val)
        if root.left:
                self.findLeaves(root.left,res)
        if root.right:
                self.findLeaves(root.right,res)