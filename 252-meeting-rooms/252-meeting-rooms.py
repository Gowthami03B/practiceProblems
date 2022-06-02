class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1,len(intervals)):#sort intervals and check if end of 1st interval < start of next interval
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True