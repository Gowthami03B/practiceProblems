class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.height = height
        self.width = width
        self.queue = deque()
        self.queue.append((0,0))
        self.food = food
        self.snake_set = set([(0,0)])
        self.dir = {"R" : (0,1),"L": (0,-1),"U":(-1,0),"D":(1,0)}
        self.gamescore = 0

    def move(self, direction: str) -> int:
        dr,dc = self.dir[direction]
        r,c = self.queue[0][0],self.queue[0][1]
        nr,nc = r+dr, c+dc
        if not (0<=nr<self.height and 0<=nc<self.width):
            return -1
        if (nr,nc) in self.snake_set and (nr,nc) != (self.queue[-1][0],self.queue[-1][1]):
            return -1
        if self.gamescore != len(self.food) and nr == self.food[self.gamescore][0] and nc == self.food[self.gamescore][1]:
                self.gamescore += 1
        else:
            tail = self.queue.pop()
            self.snake_set.remove(tail)
        self.queue.appendleft((nr, nc))
        self.snake_set.add((nr, nc))  
        return self.gamescore
            


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)