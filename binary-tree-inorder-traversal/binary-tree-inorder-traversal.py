# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # def dfs(root: Optional[TreeNode]):
        #     if root:
        #         dfs(root.left) #dfs on root to print lowest leaf left node
        #         res.append(root.val)#print it's root
        #         dfs(root.right)#print right of lowest right node
        #         return res
        # return dfs(root)
    
        res, stack = [], []
        while stack or root:
            if root:
                stack.append(root) #adding entire tree first, then whole of left subtree until the left leaf node
                root = root.left
            else:
                node = stack.pop()#pop the left most first 
                res.append(node.val) #add it to res
                root = node.right #leaf node won't have right, hence pops root next, adds root value to response, then right leaf of last root node
        return res