# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        values = []
        while head:
            values.append(head.val) #append values to list
            head = head.next
        # return values == values[::-1]#compare if list == reverse
        i,j = 0, len(values) - 1
        while(i < j):
            if values[i] == values[j]:#use 2 pointers to compare lists
                i += 1
                j -= 1
            else:
                return False
        return True
    
    #recursion
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front_pointer = head
        def check_recursively(head):
            if head is not None:
                # print("new node", head, head.next)
                if not check_recursively(head.next):#if this func returns false, then false
                    return False
                if self.front_pointer.val != head.val:#check if front == tail,else false
                    return False
                self.front_pointer =self.front_pointer.next#move front to next
            return True#other cases return true
        return check_recursively(head)