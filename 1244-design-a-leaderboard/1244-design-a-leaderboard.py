from heapq import heappush, heappop
from sortedcontainers import SortedDict

class Leaderboard1:
    
    def __init__(self):
        self.scores_map = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores_map[playerId] += score

    def top(self, K: int) -> int: #O(N log k) + O(K)(sum of all K elements)#O(N+K) - space scores and heap
        minheap = []
        for player, score in self.scores_map.items():
            heappush(minheap, (score,player))
            if len(minheap) > K:
                heappop(minheap)
        return sum([val[0] for val in minheap])

    def reset(self, playerId: int) -> None:
        self.scores_map[playerId] = 0
        
class Leaderboard:
    
    def __init__(self):
        """
         We don't have a way to construct a reverse SortedDict in Python and hence, we negate the scores before adding them to the dict (TreeMap like data structure) so that the normal in-order traversal would give us the scores in the reverse order i.e. descending order.
        """
        self.scores_map = {}
        self.sortedScores = SortedDict()#key will be score and value is no of players with that score

    #to add, if player exists, get preScore and no of player with that score, if 1, del else dec player count
    #if they don't add to dict, for sorted dict get count and increment
    def addScore(self, playerId: int, score: int) -> None:#O(log N)- Addition to BST causes O(log N)
        if playerId in self.scores_map:
            preScore = self.scores_map[playerId]
            playerCount = self.sortedScores.get(-preScore)
            if playerCount == 1:
                del self.sortedScores[-preScore]
            else:
                self.sortedScores[-preScore] = playerCount - 1
            newScore = score + preScore
            self.scores_map[playerId] = newScore
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore,0) + 1
        else:
            self.scores_map[playerId] = score 
            self.sortedScores[-score] = self.sortedScores.get(-score,0) + 1#get if score exists or 0

    def top(self, K: int) -> int: #o(k)- we iterate over keys and stop when we reach K scores - how many times the function is running for
        count, total =0,0
        for score,times in self.sortedScores.items():#loop through sorted dict
            for _ in range(times):
                total += -score#add score, since we need top k players sum of score, we keep track of count
                count += 1#counts the no of score we are summing up
                if count == K:
                    break
            if count == K:#any time count == K, we break and return
                break
        return total

    #playerId's old score count needs to be reduced by 1, if old count is 1, then del, and del from dict
    def reset(self, playerId: int) -> None:#O(log N)
        preScore = self.scores_map[playerId]
        if self.sortedScores[-preScore] == 1:
            del self.sortedScores[-preScore] 
        else:
            self.sortedScores[-preScore] -=1
        del self.scores_map[playerId]

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)