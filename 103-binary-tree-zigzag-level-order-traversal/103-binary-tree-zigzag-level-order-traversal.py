# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        if not root:
            return res
        queue = deque([root])
        count = -1
        while queue:
            count += 1
            levels = []
            for _ in range(len(queue)):
                node = queue.popleft()
                levels.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if count%2:
                res.append(levels[::-1])
            else:
                res.append(levels)
        return res
        
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        results = []
        def dfs(node, level):
            if level == len(results):#normal condition if level >=len(results); we can append the initial nodes as queue and create a new level
                results.append(deque([node.val]))#deque so we can append on both sides
            else:#else say [3,9,20,null,null,15,7], when 20 is there,level = 1, res has len 2, and for all level 1, order is right to left
                if level % 2 == 0:
                    results[level].append(node.val)
                else:
                    results[level].appendleft(node.val)
                    
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)
                
        # normal level order traversal with DFS
        dfs(root, 0)

        return results
        