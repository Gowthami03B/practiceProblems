# #complicated hit counter with binary search
# class HitCounter1:

#     def __init__(self):
#         self.keep_last_val = 0
#         self.times_hits = defaultdict(int)

#     def hit(self, timestamp: int) -> None:
#         self.keep_last_val += 1
#         self.times_hits[timestamp] = self.keep_last_val

#     def getHits(self, timestamp: int) -> int:
#         def findIdx(keys, bound):
#             start, end = 0, len(keys) - 1
#             while(start<=end):
#                 mid = (start+end)//2
#                 if keys[mid] == bound:
#                     return bound
#                 elif keys[mid] > bound:
#                     end = mid - 1
#                 else:
#                     start = mid + 1
#             return keys[mid]
#         keys = [key for key in self.times_hits.keys()]
#         print(keys)
#         #find hits between lower_bound and timestamp
#         lower_bound = timestamp - 300
#         #wrong bcs we need to subtract all prev values from running sum
#         if lower_bound <= 0:
#             return self.times_hits[findIdx(keys, timestamp)]
#         return self.times_hits[findIdx(keys, timestamp)] self.times_hits[findIdx(keys, lower_bound)]
    
class HitCounter:

    def __init__(self):
        self.hit_queue = deque()

    def hit(self, timestamp: int) -> None:
        self.hit_queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while(self.hit_queue):
            diff = timestamp - self.hit_queue[0]
            if diff >= 300:
                self.hit_queue.popleft()
            else:
                break
        return len(self.hit_queue)
    

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)