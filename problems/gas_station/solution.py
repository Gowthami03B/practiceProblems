class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
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