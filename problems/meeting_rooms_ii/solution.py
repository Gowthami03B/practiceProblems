from heapq import heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        if len(intervals) == 0:
            return 0
        roomsNeeded = []
        heappush(roomsNeeded, intervals[0][1]) #we push the end time of first meeting
        for interval in intervals[1:]: #for all subsequent meetings
            if interval[0] >= roomsNeeded[0]: #if next start interval is >= first element on heap, means the new interval can be scheduled in the same room, [4,8][10,12]
                heappop(roomsNeeded) #hence we pop
            heappush(roomsNeeded, interval[1]) #we only pop when above condition is met, else we push the new interval with it's end time
        return len(roomsNeeded)
        