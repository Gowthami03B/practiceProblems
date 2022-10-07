class BrowserHistory1:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur_index = 0
        
    def visit(self, url: str) -> None:#O(N), No of urls to be cleared
        # clear all forward history
        tail_len = len(self.history)-self.cur_index-1 #no of items to clear = total -1 - index
        while tail_len:
            self.history.pop()
            tail_len -= 1
            
        self.history.append(url)#append and increment
        self.cur_index += 1
        
    def back(self, steps: int) -> str:#O(1)
		# boundary check
        if steps > self.cur_index:#if steps > index, then can go back to only 0th page
            self.cur_index = 0
        else:
            self.cur_index -= steps#else update index-=steps
            
        return self.history[self.cur_index]
    
    def forward(self, steps: int) -> str:#O(1)
        # boundary check
        if steps >= len(self.history) - self.cur_index:#if steps >= len - index(is the current page)
            self.cur_index = len(self.history) - 1
        else:
            self.cur_index += steps
        
        return self.history[self.cur_index]
    
class DoublyLinkedList:
    def __init__(self,val=None,prev=None,next=None):
        self.val = val
        self.prev= prev
        self.next=next
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = DoublyLinkedList(homepage)
        
    def visit(self, url: str) -> None:#O(1)
        newnode = DoublyLinkedList(url)
        self.history.next = newnode
        newnode.prev= self.history
        self.history = self.history.next
        
    def back(self, steps: int) -> str:#O(steps) worst case
        while steps and self.history.prev:
            self.history = self.history.prev
            steps -= 1
        return self.history.val
    
    def forward(self, steps: int) -> str:#O(steps)worst case
        while steps and self.history.next:
            self.history = self.history.next
            steps -= 1
        return self.history.val