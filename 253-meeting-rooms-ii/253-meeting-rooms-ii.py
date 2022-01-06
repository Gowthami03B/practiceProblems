class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        freerooms = []
        heapq.heappush(freerooms, intervals[0][1])
        for i in intervals[1:]:
            if freerooms[0] <= i[0]:
                heapq.heappop(freerooms)
            heapq.heappush(freerooms, i[1])

        return len(freerooms)