"""
Given a Binary Tree, the task is to print the leaf nodes from left to right. The nodes must be printed in the order they appear from left to right.
Examples: 
 

Input :
           1
          /  \
         2    3
        / \  / \
       4  5  6  7
 
Output :4 5 6 7
"""

class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printAllLeafNodesRecursive(root):
    paths = []
    def dfs(root):
        if root:
            if not root.left and not root.right:
                paths.append(root.val)
            else:
                dfs(root.left)
                dfs(root.right)

    dfs(root)
    return paths

def printAllLeafNodesIterative(root):
    paths = []
    stack  =[(root)]
    while stack:
        root  = stack.pop()
        if root:
            if not root.left and not root.right:
                paths.append(root.val)
            else:
                stack.append(root.right)
                stack.append(root.left)

    return paths

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
# root.right.left = TreeNode(11)
# root.right.right = TreeNode(12)
print(printAllLeafNodesIterative(root))
print(printAllLeafNodesRecursive(root))
