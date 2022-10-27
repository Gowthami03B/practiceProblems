class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        d = collections.deque([i for i in range(1, n + 1)])
        while(len(d) != 1):
            d.rotate(-k) #one negative rotation == [1,2,3,4,5] becomes [2,3,4,5,1] #rotate k times so we know the friend that we are ending up with.
            d.pop()#its the last friend, popping it
        return d.pop() 
    
    
    def findTheWinner(self, n: int, k: int) -> int:
        game = [i for i in range(1 , n + 1)]#list of values
        i = 0
        while len(game) > 1:
            new_index = i + (k - 1)#new index is the friend we end up i.e i+(k-1)
            if new_index >= len(game):
                new_index = new_index % len(game)#if greater than len(game, then modulo)
            game.pop(new_index)#else we pop
            i = new_index #i the next start point is new index
        
        return game[0]