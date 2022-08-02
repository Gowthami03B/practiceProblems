class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.height = height
        self.width = width
        self.queue = deque([(0,0)])
        self.food = food
        self.snake_set = set([(0,0)])#Maintain a hashset which models the unique co-ordinates which define the snake's body.
        self.dir = {"R" : (0,1),"L": (0,-1),"U":(-1,0),"D":(1,0)}
        self.gamescore = 0

    def move(self, direction: str) -> int:
        dr,dc = self.dir[direction]
        r,c = self.queue[0][0],self.queue[0][1]
        nr,nc = r+dr, c+dc
        if not (0<=nr<self.height and 0<=nc<self.width):
            return -1
        #If the new co-ordinates collide with the snake body (except the tail which would be eventually shifted), we return -1.hence if nr,nc in snakeset and not same as old tails position
        if (nr,nc) in self.snake_set and (nr,nc) != (self.queue[-1][0],self.queue[-1][1]):
            return -1
        #that means food is available to eat
        if self.gamescore != len(self.food) and nr == self.food[self.gamescore][0] and nc == self.food[self.gamescore][1]:
                self.gamescore += 1
        else:#If no food is eaten, we add the new head and pop the current tail since the snake gets shifted by unit and the new tail is previous second last element.
            tail = self.queue.pop()
            self.snake_set.remove(tail)
        #If food is available at the head location, we add the food location as the new head. This increases the length of the snake.
        self.queue.appendleft((nr, nc))
        self.snake_set.add((nr, nc))  
        print((nr,nc), self.queue, self.snake_set)
        return self.gamescore
            


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)