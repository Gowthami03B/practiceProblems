# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        newnode= dummy
        carry = 0
        while l1 or l2:
            if l1 and l2:
                sum_num = l1.val + l2.val + carry
                carry = 0
                sum_num_str = str(sum_num)
                if len(sum_num_str) > 1:
                    carry = 1
                    newnode.next = ListNode(int(sum_num_str[1]))
                else:
                    newnode.next = ListNode(sum_num)
                l1 =l1.next
                l2=l2.next
            elif l1:
                sum_num = l1.val + carry
                carry = 0
                sum_num_str = str(sum_num)
                if len(sum_num_str) > 1:
                    carry = 1
                    newnode.next = ListNode(int(sum_num_str[1]))
                else:
                    newnode.next = ListNode(sum_num)
                l1 =l1.next
            else:
                sum_num = l2.val + carry
                carry = 0
                sum_num_str = str(sum_num)
                if len(sum_num_str) > 1:
                    carry = 1
                    newnode.next = ListNode(int(sum_num_str[1]))
                else:
                    newnode.next = ListNode(sum_num)
                l2=l2.next
            newnode = newnode.next
        if carry:
            newnode.next=ListNode(carry)
        return dummy.next
        