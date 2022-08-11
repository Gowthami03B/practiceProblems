# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        nodes_depth = defaultdict(tuple)
        def dfs(root,depth=0,par=None):
            if not root:
                return None
            nonlocal nodes_depth
            nodes_depth[root.val] = (depth,par)
            dfs(root.left,depth + 1,root.val)
            dfs(root.right,depth + 1,root.val)
        dfs(root,0)
        print(nodes_depth)
        if nodes_depth[x][0] == nodes_depth[y][0] and (nodes_depth[x][1] != nodes_depth[y][1]):
            return True
        else:
            return False
        