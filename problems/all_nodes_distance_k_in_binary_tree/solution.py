# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def setParent(root, par=None):
            if root:
                root.par = par
                setParent(root.left, root)
                setParent(root.right, root)
        setParent(root) #setParent
        queue = collections.deque([(target,0)])#adding them as a list so we can return a list
        visited = set()
        visited.add(target)
        while queue:
            if queue[0][1] == k:# if you are popping the element with k =2, that means you have explored all elements at distance k and only k=2 elements are in queue
                return [node.val for node, d in queue] #then return all in queue
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):#basically check your neighbours like graph
                if nei and nei not in visited:
                    queue.append((nei, d + 1))#if not in visited and immediate neighbout d + 1
                    visited.add(nei)
        return []
        