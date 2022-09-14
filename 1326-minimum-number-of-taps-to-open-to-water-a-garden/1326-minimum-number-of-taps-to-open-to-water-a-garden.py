class Solution:
    #Greedy solution
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i, val in enumerate(ranges):
            start,end = i-val, i+val
            if start< 0: #need not consider < 0 or > n values
                start = 0
            if end > n:
                end = n
            intervals.append([start,end])
            
        # intervals.sort(key=lambda x: (x[0], -x[1]))#sort by first asc and second in desc
        intervals.sort()
        print(intervals)
        count = i = curr= next_end = 0
        while i < len(intervals):
            while i < len(intervals) and intervals[i][0] <= curr:#if the start <= curr, update the next_end with end
                next_end = max(next_end, intervals[i][1])
                i += 1
            if next_end == curr:#if no change after above step, then no overlap hence -1 #3 [0,0,0,0]
                return -1
            curr = next_end #update curr
            count += 1#update count (min taps)
            if curr >= n:#we can cover whole garden
                return count
        return -1
    