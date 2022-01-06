class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x : x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] <= interval[0] :
                merged.append(interval)

        return True if len(merged) == len(intervals) else False