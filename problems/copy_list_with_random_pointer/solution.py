"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        visited = {}#has clones copies of nodes
        #head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
        #7's next is 13 and random is null, 13's random is 0th node i.e 7
        def deepCopy(head: 'Optional[Node]') -> 'Optional[Node]':
            if head == None:
                return None
            nonlocal visited
            if head in visited:
                return visited[head]#if the node is already created and present in visited

            node = Node(head.val, None, None)#else create a new node
            visited[head] = node#visited[currentnode] = clonedcopy
            node.next = deepCopy(head.next)#for next and random
            node.random = deepCopy(head.random)
            return node
        
        return deepCopy(head)
    
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        visited = {}
        def getClonedNode(node):
            if node:
                if node in visited:
                    return visited[node]
                else:
                    visited[node] = Node(node.val,None,None)
                    return visited[node]
            return None#if not node, return None
            
        if not head:
            return None
        old_node = head
        new_node = Node(old_node.val, None,None)#create new cloned node for head
        visited[old_node] = new_node#map current node to cloned node
        while old_node != None:
            new_node.next = getClonedNode(old_node.next)#getclones for next and random
            new_node.random = getClonedNode(old_node.random)
            old_node = old_node.next
            new_node = new_node.next
        return visited[head]