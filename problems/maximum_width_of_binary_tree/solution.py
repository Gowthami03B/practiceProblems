# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTreeBFS(self, root: Optional[TreeNode]) -> int:
        #BFS, calculate index of each node
        if root is None:
            return 0
        maxwidth = 0
        queue = collections.deque()
        queue.append((root, 0))
        while queue:
            level_len = len(queue)
            _, level_head_index = queue[0]
            for _ in range(level_len):
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*index))
                if node.right:
                    queue.append((node.right, 2*index + 1))
            
            maxwidth = max(maxwidth,index - level_head_index + 1)#we traverse through the length of the list and find difference between right most node and first node
        return maxwidth
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #BFS, calculate index of each node
        if root is None:
            return 0
        maxwidth = 0
        first_col_index = {}
        def dfs(root, depth, index):
            nonlocal maxwidth
            if root is None:
                return 
            if depth not in first_col_index:
                first_col_index[depth] = index#if depth is not in map, then add, and it would be the first node, bcs we always travel left most node first in any level
                
            maxwidth = max(maxwidth, index - first_col_index[depth] + 1)
            dfs(root.left, depth + 1, 2*index)
            dfs(root.right, depth + 1, 2*index + 1)
        
        dfs(root, 0, 0)
        return maxwidth