# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoListsRecursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val < list2.val:#[1,2,4],[1,3,4]
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:#1.next = [3,4] & [1,2,4] #1.next = [2,4],[3,4] and soon
            list2.next = self.mergeTwoLists(list2.next,list1)
            return list2
        
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)#temp node
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1#next is l1 and increment l1
                l1 = l1.next
            else:
                prev.next = l2#else next is l2 and increment l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 else l2
        return prehead.next