# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(l):
            curr = l
            prev=None
            while curr:
                temp = curr.next
                curr.next=prev
                prev = curr
                curr = temp
            return prev
        
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        # print(l1,l2)
        dummy = ListNode(-1)
        carry = 0
        new_node = dummy
        while l1 or l2:
            l1_val=l1.val if l1 else 0
            l2_val=l2.val if l2 else 0
            sum_tot = l1_val+l2_val+carry
            carry = sum_tot//10
            new_node.next=ListNode(sum_tot%10)
            new_node=new_node.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        # print(carry,l1,l2)
        if carry:
            new_node.next=ListNode(carry)
        return reverseList(dummy.next)
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # find the length of both lists
        n1 = n2 = 0
        curr1, curr2 = l1, l2
        while curr1:
            curr1 = curr1.next 
            n1 += 1
        while curr2:
            curr2 = curr2.next 
            n2 += 1
            
        # parse both lists
        # and sum the corresponding positions 
        # without taking carry into account
        # 3->3->3 + 7->7 --> 3->10->10 --> 10->10->3
        curr1, curr2 = l1, l2
        head = None
        while n1 > 0 and n2 > 0:
            val = 0
            if n1 >= n2:
                val += curr1.val 
                curr1 = curr1.next 
                n1 -= 1
            if n1 < n2:
                val += curr2.val 
                curr2 = curr2.next
                n2 -= 1
                
            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr #we get the reversed value at this point, 7 10 7 7

        # take the carry into account
        # to have all elements to be less than 10
        # 10->10->3 --> 0->1->4 --> 4->1->0
        curr1, head = head, None
        carry = 0
        while curr1:
            # current sum and carry
            val = (curr1.val + carry) % 10
            carry = (curr1.val + carry) // 10
            
            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

            # move to the next elements in the list
            curr1 = curr1.next
        
        # add the last carry
        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr

        return head