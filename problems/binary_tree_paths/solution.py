# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        #bad approach - path += '->' is bad because this will create a lot of useless strings in the heap
        #different path values would be present for different nodes as path is string and new strings are created everytime
        #say 2, 1->; 4, 1->2->, 3, 1->
        paths = []
        def dfs(root,path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += "->"
                    dfs(root.left,path)
                    dfs(root.right, path)
                    
        dfs(root,"")
        return paths
    
        #good approach, but join takes O(n)
        #different path values would not be present as it's a list and we concatenate values
        # paths = []
        # def dfs(root,path):
        #     if root:
        #         if not root.left and not root.right:
        #             path.append(str(root.val))
        #             paths.append("->".join(path))
        #         else:
        #             dfs(root.left,path + [str(root.val)])
        #             dfs(root.right,path + [str(root.val)])
        # dfs(root,[])
        # return paths
    
    def binaryTreePaths1(self, root: Optional[TreeNode]) -> List[str]:
        #with string concatenation
        # paths = []
        # stack = [(root,"")]
        # while stack:
        #     root, path = stack.pop()
        #     if root:
        #         path += str(root.val)
        #         if not root.left and not root.right:
        #             paths.append(path)
        #         else:
        #             if root.left:
        #                 stack.append((root.left, path + "->"))
        #             if root.right:
        #                 stack.append((root.right, path + "->"))
        # return paths
    
        #without string concatenation
            paths = []
            stack = [(root,0)]
            path = []
            while stack:
                root, height = stack.pop()
                if root:
                    path.append(str(root.val))
                    if not root.left and not root.right:
                        paths.append("->".join(path))
                        #we also need to remove all the last elements
                        if len(stack):
                            _, next_node_ht = stack[-1]
                            while len(path) > next_node_ht:
                                path.pop()
                    else:
                        if root.left:
                            stack.append((root.left, height + 1))
                        if root.right:
                            stack.append((root.right, height + 1))
            return paths
  
    


        