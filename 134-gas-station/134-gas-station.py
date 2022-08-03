class Solution:
    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        totaltank, currtank, start = 0,0,0
        for i in range(n):
            totaltank += gas[i] - cost[i]
            currtank += gas[i] - cost[i]
            if currtank < 0:
                start = i + 1
                currtank = 0
        return start if totaltank >= 0 else -1
    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        totalgas = 0
        min_amt = gas[0]
        min_idx = 0
        for i in range(len(gas)):
            totalgas += gas[i] - cost[i]
            if totalgas < min_amt:
                min_amt = totalgas
                min_idx = i + 1
                
        return (min_idx)%len(gas)