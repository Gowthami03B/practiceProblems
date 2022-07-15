# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycleExtraSpace(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while(head):
            if head in visited:
                return True
            visited.add(head)#add to set, if in visited, return True
            head = head.next
        return False
    
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        # The slow pointer moves one step at a time while the fast pointer moves two steps at a time.
        slow = head
        fast = head.next
        while slow != fast:#when they meet, there is a cycle
            if fast is None or fast.next is None:#no cycle and fast reaches the end
                return False
            slow = slow.next#one step
            fast = fast.next.next#2 steps
        return True