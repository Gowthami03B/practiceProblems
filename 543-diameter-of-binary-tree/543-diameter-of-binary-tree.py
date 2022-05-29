# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def calcdiameter(root) :
            if not root:
                return 0
            nonlocal diameter #The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.Use the keyword nonlocal to declare that the variable is not local.
            left = calcdiameter(root.left)
            right = calcdiameter(root.right)
            diameter = max(diameter, left + right) #calculate the max diameter at each node considering it as the main node (so it would be max(max till now, left+right))
            # print(f"{root}, height= {max(left, right)+1}, diameter ={diameter}")
            return max(left, right)+1 #at each node, we need to return the max height of the tree, i.e max of left or right + 1 for current node

        calcdiameter(root)
        return diameter