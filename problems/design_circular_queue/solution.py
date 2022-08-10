from threading import Lock
class MyCircularQueue:

    def __init__(self, k: int):
    #we store head of the queue at the front and tail at the end
    #we need to update our head index to shift our head whenever queue is dequeued, similarly we need the modulo operation to fill the front of our queue if there's space
    #formulas are normal formulas say next headval is head+1, we just add mod to it
        self.capacity = k
        self.arr =[0] * k
        self.head=0
        self.count=0 #current no of elements in queue
        self.queueLock = Lock()

    def enQueue(self, value: int) -> bool:
        with self.queueLock:# automatically acquire the lock when entering the block
            if self.isFull():
                return False
            #since it's a circular queue, we keep going to end of queue and then coming to 0th position after it exceeds capacity, hence the mod operation
            newPos= (self.head + self.count)%self.capacity
            self.arr[newPos] = value
            self.count += 1
        # automatically release the lock when leaving the block
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
         #say head=0, count=3, [1,2,3] , deleting first element, head shoud be 2
         #say head=2, count=1, [del,del,3] , deleting 3rd element, head shoud be 0, hence the formula
        self.head = (self.head + 1)%self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        print(self.arr[self.head])
        return self.arr[self.head]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        else:
            #say head=0, count=3, [1,2,3] , tail is 0+3-1%capacity
            #say head=2,count=1, tail is [del,del,3], 2+1-1%capacity
            tailPos = (self.head + self.count-1)%self.capacity
            return self.arr[tailPos]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()