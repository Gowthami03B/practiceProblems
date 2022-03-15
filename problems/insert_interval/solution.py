class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #intervals = [[1,3],[6,9]], newInterval = [2,5]
        newstart, newend = newInterval
        idx, n = 0, len(intervals)
        output = []
        # add all intervals starting before newInterval
        while(idx < n and newstart > intervals[idx][0]):
            output.append(intervals[idx])
            idx += 1
           
         # add newInterval
        # if there is no overlap, just add the interval
        if not output or output[-1][1] < newstart:
            output.append(newInterval)
        # if there is an overlap, merge with the last interval
        else:
            output[-1][1] = max(output[-1][1], newend)
        
        # add next intervals, merge with newInterval if needed   
        while(idx < n):#array index until n - 1
            interval = intervals[idx]
            start, end = interval
            idx += 1 #incrementing for next iteration
            # if there is no overlap, just add an interval
            if output[-1][1] < start: #only < and not <=, for proper merge to happen
                output.append(interval)
            else:
            # if there is an overlap, merge with the last interval
                output[-1][1] = max(output[-1][1], end)
        return output