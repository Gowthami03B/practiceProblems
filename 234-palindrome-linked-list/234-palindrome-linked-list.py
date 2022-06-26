# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        # return values == values[::-1]
        i,j = 0, len(values) - 1
        while(i < j):
            if values[i] == values[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front_pointer = head
        def check_recursively(head):
            if head is not None:
                if not check_recursively(head.next):
                    return False
                if self.front_pointer.val != head.val:
                    return False
                self.front_pointer =self.front_pointer.next
            return True
        return check_recursively(head)