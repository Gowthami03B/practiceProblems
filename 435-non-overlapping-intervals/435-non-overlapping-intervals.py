from heapq import heappush, heappop
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # if two intervals are overlapping, we want to remove the interval that has the largest end -- the longer interval will always overlap with more or the same number of future intervals compared to the shorter one
        m =len(intervals)
        if m == 1 or m == 0:
            return 0
        intervals.sort(key=lambda x: x[1])#hence sort by second interval in asc order
        endInterval = intervals[0][1]
        count = 1
        for i in range(1,m):
            if intervals[i][0] >= endInterval:#if the next interval is contiguous, update endInterval
                endInterval = intervals[i][1]
                count += 1
        return m - count#we count no of non-overlapping intervals, hence removal is m - count