# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        """
        Use 2 pointers both will point to the previous node of head, (can be achieved with dummy node).
        Keep a gap of n + 1 nodes between first and second pointers
        By the time second reaches the end, first would be n + 1 nodes away from end which is needed.Now first pointer is positioned at previous node of the node to be deleted. You need the first node to be positioned at node before nth node, so u can do this first.next=first.next.next
        """
        dummy = ListNode(-1)
        first = dummy
        second=dummy
        dummy.next=head
        for i in range(n+1):
            second = second.next
            
        print(second)
        while(second):
            first = first.next
            second=second.next
        print(first,second)
        
        first.next = first.next.next#delete the middle node
        return dummy.next
        