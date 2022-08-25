from heapq import heappush,heappop
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: 
            return 0
        #or len(intervals) < 1:
        #    return 0
        intervals.sort(key=lambda x : x[0])
        minheap = []
        rooms_needed = 0
        #heappush(minheap,intervals[0][1])
        for interval in intervals[:]:
            if minheap and minheap[0] <= interval[0]:
                heappop(minheap)
            else:
                rooms_needed += 1
            heappush(minheap,interval[1])
        return rooms_needed