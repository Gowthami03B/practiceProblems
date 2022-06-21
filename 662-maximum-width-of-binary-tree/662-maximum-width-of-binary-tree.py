# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
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
    
    