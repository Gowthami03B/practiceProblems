class Node:
 
# Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null
        self.prev = None # Initialize prev as null       
         
# Stack class contains a Node object
"""
1. push() : Insert the element into Stack and assign the top pointer to the element. 
2. pop() : Return top element from the Stack and move the top pointer to the second element of the Stack. 
3. top() : Return the top element. 4. size() : Return the Size of the Stack. 
5. isEmpty() : Return True if Stack is Empty else return False. 6. printstack() : Print all elements of the stack.
"""
class Stack:
    # Function to initialize head
    def __init__(self):
        self.head = None

    def push(self,val):#push the element as top of the DLL
        if self.head is None:
            self.head = Node(val)
        else:
            newNode = Node(val)#create new node
            self.head.prev = newNode#head's prev is new node
            newNode.next = self.head#newnode's next is head
            newNode.prev = None#newnode's prev is none
            self.head = newNode#new node is head
            
        
    def pop(self):#Pop the top element
        if self.head is None:
            return None
        if self.head.next is None:
            temp = self.head.data
            self.head = None
            return temp
        else:
            temp = self.head.data 
            self.head = self.head.next
            self.head.prev = None
            return temp

    def topElement(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        if self.head is None:
            return 0
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def printStack(self):
        temp = self.head
        count = 0
        while temp:
            print(temp.data, end ="->")
            temp = temp.next
        
# Code execution starts here        
if __name__=='__main__':
 
# Start with the empty stack
  stack = Stack()
 
# Insert 4 at the beginning. So stack becomes 4->None
  print("Stack operations using Doubly LinkedList")
  stack.push(4)
 
# Insert 5 at the beginning. So stack becomes 4->5->None
  stack.push(5)
 
# # Insert 6 at the beginning. So stack becomes 4->5->6->None
  stack.push(6)
 
# Insert 7 at the beginning. So stack becomes 4->5->6->7->None
  stack.push(7)
 
# Print the stack
  stack.printStack()
 
# Print the top element
  print("\nTop element is ", stack.topElement())
 
# # Print the stack size
  print("Size of the stack is ", stack.size())
 
# # pop the top element
  stack.pop()
 
# # pop the top element
  stack.pop()
   
# # two elements are popped
# # Print the stack
  stack.printStack()
   
# Print True if the stack is empty else False
  print("\nstack is empty:", stack.isEmpty())
