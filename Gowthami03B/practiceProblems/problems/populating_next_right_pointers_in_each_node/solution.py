"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        #with O(N) space
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size-1:#if i < size-1, then populate next
                    node.next=queue[0]
                if node.left:
                    queue.append(node.left)#to back
                if node.right:
                    queue.append(node.right)
        return root
        
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        leftmost = root
        while leftmost.left:#while left exists
            head = leftmost
            while head:
                head.left.next = head.right#between child pointers under same parent
                if head.next:
                    head.right.next = head.next.left#need to point left subtrees right to right subtrees left
                head = head.next#progress head
            leftmost = leftmost.left#end of level so leftmost=leftmost.left
        return root
            