# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
brute force -
say 6,5
- traverse from root to p - store path in set - [3,5,6]
- traverse from root to q - [3,5]
last common one is the least common ancestor

say 0,8
- traverse from root to 0, will take us through - [3,5,6,2,7,4,1,0,8],we will also have all these nodes

Optimal Solution when p,q are treenodes-
- set Parent for nodes
- traverse through p's parent and mark as visited
- traverse from q to parent, when we find a node of q's parent in visited will be the lowest common

if p,q are values instead of treenodes
- need to find if p and q exist in tree - we check if root is in p,q is so, return 1 else 0
- since we are finding 2 target nodes, total sum would be 2 and the root at which it becomes 2 is the lowest common acestor
- if so, find the lowest common ancestor
"""

class Solution:
    def __init__(self):
        self.visited = set()
        self.ancestor = None
        #Approach 1
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.setParent(root)#setParent
        while p is not None:
            self.visited.add(p.val)
            p = p.parent#traverse p's parents
        while q is not None:
            if q.val in self.visited:#if q parent already in visited, return q
                return q
            q = q.parent#traverse q's parents
        return None
    
    def setParent(self, root, par=None):
        if root is None:
            return
        root.parent = par
        self.setParent(root.left, root)
        self.setParent(root.right, root)
        
    def dfs(self,root):
        if root is None or self.ancestor:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        total = left + right + (root in self.targets)
        if total == 2 and not self.ancestor:#the total becomes 2 when we found both the roots and at the common ancestor
            self.ancestor = root
        return total
        
    #Approach2
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.targets = [p,q]#this works even in p,q are given as values and not nodes
        self.dfs(root)
        return self.ancestor
        
    
        