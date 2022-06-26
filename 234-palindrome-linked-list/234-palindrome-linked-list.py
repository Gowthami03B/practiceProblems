# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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