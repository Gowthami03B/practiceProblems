# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #to optimize below code, we can convert linked list to array and convert sorted array to BST in O(N) time and space
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        # print(head)
         #O(log N) operation for N elements hence O(N log N)
        #basically head has first half and slow_ptr/mid has second half
        #node.left=head, node.right=mid as per BST
        mid = self.findMiddle(head)#-10 -3 0 5 9, mid would be 0 5 9 and head becomes -10 -3, node.left([-10 -3]), head becomes -10, mid is -3
        node= TreeNode(mid.val)
        if head == mid:
            return node#if head has only 1 value
        node.left=self.sortedListToBST(head)
        node.right=self.sortedListToBST(mid.next)#mid.next as mid is already made node
        return node

    def findMiddle(self,head):
        #O(log N) operation
            prevPtr = None
            slow_ptr=head
            fast_ptr=head
            while fast_ptr and fast_ptr.next:#standard code for finding middle
                prevPtr =slow_ptr 
                slow_ptr=slow_ptr.next
                fast_ptr=fast_ptr.next.next
            if prevPtr:
                prevPtr.next=None#setting next half of head to none
                #when we change the next val, since we shallow copy head also changes
            return slow_ptr#has the second half