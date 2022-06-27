# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        #1->2->3 changed to 3->2->1
        while(head):
            temp = head.next #assign next val to temp to recover later
            head.next = prev #1.next = None - changes head, but this same should be in prev, next iteration, 2.next is 1.None, hence we have 2->1->none, next iteration, 3.next is 2.1.None, hence we have 3->2->1->none
            print(head,prev,"prev")
            prev = head#hence prev = head
            print(prev, "prev after changing")
            head = temp#continue iteration on next val hence head = temp
        return prev
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #1->2->3 change to 3->2->1
        #stack - [2,func(3),1,func(2)]
        #3 is last node, hence returns head which is 3
        #p becomes 3, now we need to make 2->3 as 3->2->None, so head.next.next i.e 2.next(3).next should be 2 and 2.next should be none
        #we return p, i.e the modified reversed linked list at each point
        if (not head) or (not head.next):
            return head
        # print(head)
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        # print("returned", p)
        return p