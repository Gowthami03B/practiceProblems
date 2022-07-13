from collections import OrderedDict
class LRUCache():#instantiate with ordereddict object
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


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)