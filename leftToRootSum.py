class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def printleaftorootsum(root):
    paths = []
    def dfs(root,path):
        if root:
            path += root.val
            if not root.left and not root.right:
                paths.append(path)
            else:
                dfs(root.left, path)
                dfs(root.right, path)

    dfs(root, 0)
    return paths

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = TreeNode(None)
# root.left.right = TreeNode(None)
# root.right.left = TreeNode(None)
root.right.right = TreeNode(5)
