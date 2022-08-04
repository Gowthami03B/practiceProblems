import collections
class Node:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightViewBT(root):
    queue = collections.deque([(root)])
    res = []

    while queue:
        k = len(queue)
        while k > 0:
            k -= 1
            node = queue.popleft()
            if k == 0:
                res.append(node.val)
            if node.left:
                queue.append((node.left))
            if node.right:
                queue.append((node.right))
    return res

def leftViewBT(root):
    queue = collections.deque([(root)])
    res = []
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if i == 0:
                res.append(node.val)
            if node.left:
                queue.append((node.left))
            if node.right:
                queue.append((node.right))
    return res

def leftViewRecursive(root):
    if not root:
        return
    level_map = collections.defaultdict(int)
    def helper(root, level):
        if len(level_map) == level and level not in level_map:
            level_map[level] = root.val
        if root.left:
            helper(root.left, level + 1)
        if root.right:
            helper(root.right, level + 1)
    
    helper(root,0)
    return level_map.values()

def leftViewRecursive1(root):
    if not root:
        return
    levels =[]
    def helper(root, level):
        if not root:
            return
        if len(levels) == level:
            levels.append(root.val)
        if root.left:
            helper(root.left, level + 1)
        if root.right:
            helper(root.right, level + 1)
    
    helper(root,0)
    return levels

root = Node(4)
root.left = Node(5)
root.right = Node(2)
root.right.left = Node(3)
root.right.right = Node(1)
root.right.left.left = Node(6)
root.right.left.right = Node(7)
print(leftViewRecursive1(root))
print(leftViewBT(root))

# print(rightViewRecursive(root))
