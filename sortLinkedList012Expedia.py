"""
Given a linked list containing 0's, 1's, and 2's, sort the linked list by doing a single traversal of it.

For example,

Input:  0 —> 1 —> 2 —> 2 —> 1 —> 0 —> 0 —> 2 —> 0 —> 1 —> 1 —> 0 —> NULL
 
Output: 0 —> 0 —> 0 —> 0 —> 0 —> 1 —> 1 —> 1 —> 1 —> 2 —> 2 —> 2 —> NULL
"""
class LinkedList:
    def __init__(self, data=None, next=None):
        self.val = data
        self.next = next

    def printList(self,head):
        if not head:
            return None
        while(head):
            print (str(head.val),end=" ") 
            head = head.next
        print()

class SortList:
    def __init__(self):
        pass
    def sortLinkedList(self,head):
        if not head or not head.next:
            return head
        count = [0,0,0]
        curr = head
        while curr:
            count[curr.val] += 1
            curr = curr.next
        print(count)
        curr = head
        i = 0
        while curr:
            if count[i] == 0:
                i += 1
            curr.val = i
            count[i] -= 1
            curr = curr.next
        return head

    def sortLinkedListOneTraversal(self,head):
        if not head or not head.next:
            return head

        first =LinkedList()
        second =LinkedList()
        third =LinkedList()

        zero =first
        # print(zero is first)
        one=second
        # print(one is second)
        two=third
        # print(two is third, two == third)
        curr = head
        while(curr):
            if curr.val == 0:
                zero.next = curr
                zero = zero.next
            elif curr.val == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
                # print(two.next is second.next, two.next == second.next)
            curr = curr.next
            # print(first,second,third)
        zero.next = second.next if second.next else third.next
        one.next = third.next
        two.next = None
        return first.next
keys = [1, 2, 0, 0, 1, 2, 1, 2, 1]
keys1=[1,1,2]
head = None
for i in reversed(range(len(keys))):
    head = LinkedList(keys[i], head)

sortobj = SortList()
head.printList(sortobj.sortLinkedListOneTraversal(head))
