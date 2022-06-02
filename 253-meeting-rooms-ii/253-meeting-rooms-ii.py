from heapq import heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        if len(intervals) == 0:
            return 0
        roomsNeeded = []
        heappush(roomsNeeded, intervals[0][1])
        for interval in intervals[1:]:
            if interval[0] >= roomsNeeded[0]:
                heappop(roomsNeeded)
            heappush(roomsNeeded, interval[1])
        return len(roomsNeeded)
        
    def minMeetingRoomsBruteForce(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        roomsNeeded  = 0
        if len(intervals) > 0:
            roomsNeeded += 1
            currMinEndTime = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1] and intervals[i][0] >= currMinEndTime:
                continue
            elif intervals[i][0] < intervals[i-1][1] and intervals[i][0] < currMinEndTime:
                roomsNeeded += 1
                currMinEndTime = min(currMinEndTime, intervals[i-1][1])
            else:
                if roomsNeeded == 0:
                    roomsNeeded += 1
                continue
        return 1 if roomsNeeded == 0 else roomsNeeded