# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum1(self, head: Optional[ListNode]) -> int:
        """
        try dividing the list in half and reverse the second half
        Use two different pointers pointing to the first nodes of the two halves of the linked list. The second pointer will point to the first node of the reversed half, which is the (n-1-i)th node in the original linked list. By moving both pointers forward at the same time, we find all twin sums.
        """
        #The thing is that curr is not a copy of the original (node or list). It is a name you give for a given node that is in the original list, if you change curr.next or curr.val, values change in the head as well.
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
            #below code changes the head node as well as secondhalf is a pointer to the head node and a linked list node can change in two ways - by changing val/next
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
        
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return -1
        
        max_sum = 0
        def find_second_half(head):
            slow_ptr, fast_ptr=head,head
            prev_ptr=None
            while fast_ptr and fast_ptr.next:
                prev_ptr=slow_ptr
                slow_ptr=slow_ptr.next
                fast_ptr=fast_ptr.next.next
            
            prev_ptr.next=None
            return slow_ptr
        
        def reverse(node):
            prev=None
            while node:
                temp_next = node.next
                node.next=prev
                prev=node
                node =temp_next
            return prev
    
        second_half = find_second_half(head)
        # print(second_half)
        reversed_second_half=reverse(second_half)
        # print(reversed_second_half,head)
        
        while head and reversed_second_half:
            max_sum = max(max_sum,head.val+reversed_second_half.val)
            head = head.next
            reversed_second_half = reversed_second_half.next
        return max_sum
            