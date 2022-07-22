class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dir = [(-2,1),(2,1),(1,2),(1,-2),(2,-1),(-2,-1),(-1,-2),(-1,2)]#8 possible moves
        def bfs():
            queue = deque([(0,0)])#start with 0,0
            visited = set()
            visited.add((0,0))
            steps = 0
            while queue:
                curr_lvl = len(queue)#after we traverse every level we would moved in the next current direction to reach our destination
                for _ in range(curr_lvl):
                    r,c = queue.popleft()#for all queue elements at each level, we travel in 8 possible directions and add them to queue, visited
                    if (r,c) == (x,y):
                        return steps
                    for nr,nc in dir:
                        dr, dc = r+nr, c+nc
                        if (dr,dc) not in visited:
                            queue.append((dr,dc))
                            visited.add((dr,dc))
                steps += 1#hence we increment count after every level  
        return bfs()