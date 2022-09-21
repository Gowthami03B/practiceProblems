# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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
        
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        newnode= dummy
        carry = 0
        while l1 or l2:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            sum_num = l1Val+l2Val+carry
            carry = sum_num//10
            newnode.next = ListNode(sum_num%10)
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            newnode = newnode.next
            
        if carry:
            newnode.next=ListNode(carry)
        return dummy.next
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_num = l1.val+l2.val
        nodeVal, carry = sum_num%10, sum_num//10
        newnode = ListNode(nodeVal)
        if l1.next or l2.next or carry:
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val += carry
            newnode.next = self.addTwoNumbers(l1,l2)
        return newnode