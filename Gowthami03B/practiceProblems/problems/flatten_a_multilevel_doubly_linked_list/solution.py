
# # Definition for a Node.
# class Node:
#     def __init__(self, val, prev, next, child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child

class Solution:
    def flattenRecursive(self, head):
        if not head:
            return head

        temp = Node(None,None,head,None)
        def dfs(node, parent):
            if not node:
                return parent
            node.prev= parent
            parent.next=node
            tempNext = node.next
            tail = dfs(node.child,node)
            node.child=None
            return dfs(tempNext,tail)
        dfs(head,temp)

        # # detach the pseudo head from the real head
        temp.next.prev = None
        return temp.next

    def flatten(self, head):
        if not head:
            return
        pseudoHead = Node(0,None,head,None)
        prev = pseudoHead #prev of head to start with

        stack = []
        stack.append(head)
        while stack:
            curr = stack.pop()

            prev.next = curr #prev.next would be current node
            curr.prev = prev #curr.prev would be prev node

            if curr.next:
                stack.append(curr.next)#we add the next first as we pop the last element
 
            if curr.child:
                stack.append(curr.child)
                # don't forget to remove all child pointers.
                curr.child = None

            prev = curr#current node is the prev in next iteration
        # detach the pseudo head node from the result.
        pseudoHead.next.prev = None
        return pseudoHead.next