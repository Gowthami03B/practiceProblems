# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        try dividing the list in half and reverse the second half
        Use two different pointers pointing to the first nodes of the two halves of the linked list. The second pointer will point to the first node of the reversed half, which is the (n-1-i)th node in the original linked list. By moving both pointers forward at the same time, we find all twin sums.
        """
        curr = head
        count_nodes = 0
        while(curr):
            count_nodes += 1
            curr = curr.next
        # print(count_nodes)#calculate no of nodes
        mid = count_nodes //2
        tmp, secondhalf = 0, head
        while tmp < mid:
            tmp += 1
            secondhalf = secondhalf.next #to get second half 
        # print(secondhalf)
        
        #reverse second half
        reversehalf = None
        #[6,3,4], we do 6->None first, then 3->6->None and 4->3>6>None
        while(secondhalf):
            nextnode = secondhalf.next #copying next into temporary
            secondhalf.next = reversehalf #initially reversehalf is none, assign it to second.next 
            reversehalf = secondhalf#assign secondhalf to reverse
            secondhalf = nextnode#continue iteration on second's next stored in temporary
        # print(reversehalf,head)#reverse will have reversed value
        maxValue = 0
        
        while head and reversehalf:#while head/rev part are not empty, calculate sum
            maxValue = max(maxValue, head.val + reversehalf.val)
            head = head.next
            reversehalf = reversehalf.next
        return maxValue
        
        
            