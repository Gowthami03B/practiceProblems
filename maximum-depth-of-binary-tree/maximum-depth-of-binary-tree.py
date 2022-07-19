from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #One could traverse the tree either by Depth-First Search (DFS) strategy or Breadth-First Search (BFS) strategy Here we demonstrate a solution that is implemented with the DFS strategy (in order traversal, bcs we go to root, then left, then its children, pop back to root and go to right) and recursion.
            # if root is None:
            #     return 0
            # left  = self.maxDepth(root.left)
            # right = self.maxDepth(root.right)
            # print(root,left,right)
            # return max(left, right) + 1#plus 1 is for root
        # BFS on a tree is level order traversal, BFS == queue
        # if root is None:
        #         return 0
        # queue = deque([root])
        # levels = 0
        # while(queue):
        #     for i in range(len(queue)): #we need to finish whole level, hence loop through all nodes in the level
        #         node = queue.popleft()
        #         print(node)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     levels += 1
        # return levels
        #iterative DFS - pre order traversal, root, left , right
#         stack = [[root,1]]
#         res = 0
#         while(stack):
#             node, depth = stack.pop()
#             print(node, depth)
#             if node:
#                 res = max(res, depth)
#                 stack.append([node.right,depth+1])
#                 stack.append([node.left,depth+1])
#         return res
    
    #Level order traversal
        if root is None:
            return 0
        queue = deque([root])
        depth = 0
        while(queue):
            depth += 1# 9,5, depth = 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left) 
                if node.right:
                    queue.append(node.right)
        return depth
