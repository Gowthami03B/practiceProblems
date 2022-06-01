class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        rows, cols = len(maze), len(maze[0])
        queue = collections.deque()
        queue.append(start)
        visited = set()
        visited.add((start[0],start[1]))
        
        while(queue):
            r, c = queue.popleft()
            if [r,c]  == destination:
                return True
            dir = [[1,0],[0,1],[-1,0],[0,-1]]       
            for dr, dc in dir:
                nr, nc = r, c
                while(nr in range(rows) and nc in range(cols) and maze[nr][nc] == 0):#iteratively checking possible ways in each direction, when we hit wall, we retrace our steps and add it to queue if it needs to be explored
                    nr+=dr
                    nc+=dc
                #if it hits a wall, then above loop will stop, add the possible coordinate before hitting wall to visited and queue
                nr-=dr
                nc-=dc
                if((nr,nc) not in visited):
                    visited.add((nr,nc))
                    queue.append([nr,nc])
        
        return False
