from heapq import heappush, heappop
class Leaderboard:

    def __init__(self):
        self.scores_map = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores_map[playerId] += score

    def top(self, K: int) -> int:
        minheap = []
        for player, score in self.scores_map.items():
            heappush(minheap, (score,player))
            if len(minheap) > K:
                heappop(minheap)
        return sum([val[0] for val in minheap])

    def reset(self, playerId: int) -> None:
        self.scores_map[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)