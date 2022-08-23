# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #O(N log k),O(k),head has O(N-total nodes)-atmost k elements in heap at everytime ; k is number of linked lists, N is no of nodes
        #adding heads to list with indices
        #[[1,4,5],[1,3,4],[2,6]]
        #heap has [(1, 0), (1, 1), (2, 2)] initially
        heap = [(lists[i].val,i) for i in range(len(lists)) if lists[i]]
        heapq.heapify(heap)
        head = None
        while heap:
            # print(heap,head)
            top_element = heapq.heappop(heap)#get top
            node = ListNode(top_element[0])
            index = top_element[1]
            if not head:#for the first time
                head = node
                trav = head#this is like temp on head
            else:
                trav.next = node
                trav = trav.next
                
            if lists[index].next:#lists[0].next is the first linkedlist head.next
                #here after 1,0 is popped, 4,0 is added to heap - [(1, 1), (2, 2), (4, 0)] and so on
                lists[index] = lists[index].next#update it
                heapq.heappush(heap, (lists[index].val, index))#add to heap
        return head          
    
    