# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(0)#temp node to hold a prev val
        temp.next = head#temp.next will point to head and temp is prev
        prev, curr = temp, head
        while(curr):
            if not curr:
                return
            if curr.val == val:
                prev.next = curr.next#when a match is found, prev.next = curr.next, it removes the curr value
            else:
                prev = curr#else update prev value
            curr = curr.next
        # print(head, temp)
        """
        ListNode{val: 7, next: ListNode{val: 7, next: ListNode{val: 7, next: ListNode{val: 7, next: None}}}} ListNode{val: 0, next: None}
- not modifying the head but using temp
        """
        return temp.next