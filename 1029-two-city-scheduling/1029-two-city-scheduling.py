from heapq import heappush,heappop
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
            countA, countB, tot_len, total_cost = 0, 0, len(costs)//2, 0
            heap = []
            for cost in costs:
                diff = abs(cost[1] - cost[0])
                heappush(heap, (-diff, cost))

            while heap and countA < tot_len and countB < tot_len:
                _, cost = heappop(heap)
                if cost[0] <= cost[1]:
                    countA += 1
                    total_cost += cost[0]
                else:
                    countB += 1
                    total_cost += cost[1]

            # Remaining elements
            index = 0 if countA < countB else 1
            total_cost += sum([ele[1][index] for ele in heap])
            return total_cost