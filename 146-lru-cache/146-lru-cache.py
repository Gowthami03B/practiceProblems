from collections import OrderedDict
class LRUCache1():#instantiate with ordereddict object
    """
    Ordered dictionary somehow can be used in the place where there is a use of hash Map and queue. It has characteristics of both into one. Like queue, it remembers the order and it also allows insertion and deletion at both ends
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ordered_map = OrderedDict()

    #whenever we get a val, we need to move that to the end as it's recently called
    def get(self, key: int) -> int:
        if key not in self.ordered_map:
            return -1
        self.ordered_map.move_to_end(key)
        return self.ordered_map[key]

    #when we put a value, if its in self, then move to end and update value else add new value, if len > capacity, remove from first
    def put(self, key: int, value: int) -> None:
        if key in self.ordered_map:
            self.ordered_map.move_to_end(key)
        self.ordered_map[key] = value
        if len(self.ordered_map) > self.capacity:
            self.ordered_map.popitem(last = False)
            
class LinkedNode():
    def __init__(self):
        self.key =None
        self.val = None
        self.prev = None
        self.next=None
    
class LRUCache():
    #we need O(1) hence hashmap,but we can't track least recently used, hence doubly linked list as add/remove from the head and tail is O(1); we add the most recently accessed node after head and remove the least recently used ones before tail
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ordered_map = {}
        self.list_size = 0
        #create a linked list to store values and maintain the least used values at tail and highly used ones near head
        self.head,self.tail = LinkedNode(),LinkedNode()#pseudo head and tail to mark boundary
        self.head.next = self.tail
        self.tail.prev=self.head
        
    def add_node(self,node):#O(1)
        next_node = self.head.next
        next_node.prev = node
        self.head.next = node
        node.next = next_node
        node.prev = self.head
        
    def remove(self,node):#O(1)
        prev= node.prev #get prev
        next_node = node.next#get next
        prev.next = next_node #prev.next would be next_node
        next_node.prev =prev#next_node's prev would be prev
        
    def move_to_end(self,node):
        #need to remove node from current position
        self.remove(node)
        #add node after head - recently used
        self.add_node(node)

    def get(self, key: int) -> int:
        node = self.ordered_map.get(key,None)
        if not node:
            return -1
        self.move_to_end(node)#move to end of linked list
        return node.val
    
    def pop_tail(self):
        node = self.tail.prev
        self.remove(node)
        return node

    def put(self, key: int, value: int) -> None:
        node = self.ordered_map.get(key)
        if not node:
            new_node = LinkedNode()
            new_node.key=key
            new_node.val = value
            self.add_node(new_node)
            self.ordered_map[key] = new_node
            self.list_size += 1
            if self.list_size > self.capacity:
                tail = self.pop_tail()
                del self.ordered_map[tail.key]
                self.list_size -=1
        else:
            node.val = value
            self.move_to_end(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)