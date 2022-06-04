from heapq import heappush, heappop
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        times = []
        for i in range(len(startTime)):
            times.append([startTime[i],endTime[i],profit[i]])
        times.sort()
        jobs = []
        maxProfit = 0
        nonoverlap_profit = 0
        for start, end, currprofit in times:
            while jobs and jobs[0][0] <= start:#for every nonoverlapped interval
                prevjob_end, prevjob_profit = heappop(jobs)
                nonoverlap_profit = max(nonoverlap_profit, prevjob_profit)
            #for all overlapped intervals
            heappush(jobs, (end,currprofit + nonoverlap_profit))
            maxProfit = max(maxProfit,currprofit + nonoverlap_profit)
        return maxProfit
    
#     Add every overlapped intervals in heap.
# \U0001f449 If there is no overlap intervals then pop the element and find profit till that point.
# \U0001f449 Repeat this to find max-profit till last.
    def jobScheduling1(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        jobs = sorted([(startTime[i],endTime[i],profit[i]) for i in         range(len(startTime))])
        heap=[]
        cp,mp = 0,0                           # cp->current profit, mp-> max-profit
        for s,e,p in jobs:
            while heap and heap[0][0]<=s:
                et,tmp = heapq.heappop(heap)
                cp = max(cp,tmp)
            heapq.heappush(heap,(e,cp+p))
            mp = max(mp,cp+p)

        return mp