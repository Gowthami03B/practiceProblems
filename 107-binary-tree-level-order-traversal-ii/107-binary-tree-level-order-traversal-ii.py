# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom1(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
            
        helper(root,0)
        return levels[::-1]
    
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
            queue=collections.deque([(root,1)])
            dic=collections.defaultdict(list)
            res=[]
            while queue:
                root,level=queue.popleft()
                if not root:
                    continue
                dic[level].append(root.val)
                if root.left:
                    queue.append((root.left,level+1))
                if root.right:
                    queue.append((root.right,level+1))
            for key in sorted(dic,reverse=True):
                res.append(dic[key])
            return res

        