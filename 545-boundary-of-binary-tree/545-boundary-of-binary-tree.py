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
        #One simple approach is to divide this problem into three subproblems- left boundary, leaves and right boundary.
        #Another approach we can observe that our problem statement is very similar to the Preorder traversal using some flags to keep track of left,right boundaries or leaves

        left_boundary = self.findleft(root.left)#leftside
        right_boundary = self.findright(root.right)#rightside
        leaves=[]
        if root.left or root.right:
            self.findLeaves(root,leaves)
        res += left_boundary + leaves + right_boundary
        return res
        
    def isleaf(self,root):
        return not root.left and not root.right
    
    #We keep on traversing the tree towards the left and keep on adding the nodes in the res array, provided the current node isn't a leaf node, else stop we found left boundary
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
    
    #same for right
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
        return res[::-1]#need right boundary in reverse order
    
    def findLeaves(self,root,res):
        if root and self.isleaf(root):#if leaf
            res.append(root.val)
        if root.left:
                self.findLeaves(root.left,res)
        if root.right:
                self.findLeaves(root.right,res)