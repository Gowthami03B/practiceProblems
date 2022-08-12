class Bucket:
    def __init__(self):
        self.bucket=[]
        
    def get(self,key):
        for k,v in self.bucket:
            if key == k:
                return v
        return -1
    
    def remove(self,key):
        for idx,kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket.pop(idx)
        
    def updateBucket(self,key,value):
        isFound = False
        for i,kv in enumerate(self.bucket):
            if key == kv[0]:
                isFound = True
                self.bucket[i] = (key,value)
                break
        if not isFound:
            self.bucket.append((key,value))
                
class MyHashMap:

    def __init__(self):
        self.map_size=2069 #prime number as they are only divisible 1 and themselves, resulting in less hash collisions
        self.hashmap=[Bucket() for _ in range(self.map_size)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.map_size
        self.hashmap[hash_key].updateBucket(key,value)

    def get(self, key: int) -> int:
        hash_key = key % self.map_size
        return self.hashmap[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.map_size
        self.hashmap[hash_key].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)