from heapq import heappush,heappop
class Solution:
    def twoCitySchedCost1(self, costs: List[List[int]]) -> int:
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
        
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # we sort and after this we get the lowest costs associated with city A first
        costs.sort(key = lambda x : x[0] - x[1])
        print(costs)
        total = 0
        n = len(costs) // 2
        # To optimize the company expenses,
        # send the first n persons to the city A (lowest cost for A)
        # and the others to the city B
        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
        return total