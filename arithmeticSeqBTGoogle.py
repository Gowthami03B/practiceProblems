"""
Given a binary tree, return the maximum length of the path which is a valid arithmatic progression sequence. A path in the tree starts at the root node and ends at the leaf node. Tree can have multiple valid arithmatic progression sequence paths, return the max length of all.

          2
       /     \
      0       4
    /   \   /    \
  -2    -2 10     6
 /   \           /   \
9    -4       -1    8

Valid AP paths - 2 0 -2 -4 - diff between nodes is 2
Valid AP paths - 2 0 -2 - diff between nodes is 2
Valid AP paths - 2 4 6 8 - diff between all nodes is -2

max_len = 4
"""

class newNode:

	# Construct to create a new node
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		
# Function to find sum of all the element
def arithmeticSeq(root):
    res = 0
    if not root:
        return 0
    def dfs(root,target, maxDepth):
        nonlocal res
        # breakpoint()
        if root is None:
            return
        if root.left:
            if target == abs(root.val - root.left.val):
                left =  dfs(root.left, abs(root.val - root.left.val), maxDepth + 1)
        if root.right:
            if target == abs(root.val - root.right.val):
                right =  dfs(root.right, abs(root.val - root.right.val), maxDepth + 1)
        res = max(maxDepth, res)
    if root.left:
        dfs(root.left, abs(root.val - root.left.val), 2)
    if root.right:
        dfs(root.right, abs(root.val - root.right.val), 2)
    return res

def arithmeticSeqApproach2(root):
    if not root:
        return 0

    max_len = 0
    def dfs(node, curr_len, delta, target):
        if node.val != target:
            return
        elif not node.left and not node.right:
            max_len = max(max_len, curr_len)
        else:  
            if node.left:
                dfs(node.left, curr_len + 1, delta, node.val - target)
            else:
                dfs(node.right, curr_len + 1, delta, node.val - target)
    if root.left:
        delta = root.val - root.left.val
        dfs(root, 1, delta, root.val - delta)
    if root.right:
        delta = root.val - root.right.val
        dfs(root, 1, delta, root.val - delta)

    return max_len
# Driver Code
if __name__ == '__main__':
    root = newNode(2)
    root.left = newNode(0)
    root.right = newNode(3)
    root.left.left = newNode(-2)
    root.left.right = newNode(-2)
    root.right.left = newNode(10)
    root.right.right = newNode(4)
    root.left.left.left = newNode(9)
    root.left.left.right = newNode(-1)
    root.right.right.left = newNode(-1)
    root.right.right.right = newNode(5)

print(arithmeticSeqApproach2(root))

