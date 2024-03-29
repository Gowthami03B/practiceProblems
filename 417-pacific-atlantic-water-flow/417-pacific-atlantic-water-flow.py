class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
    
        pacific_queue= deque()
        atlantic_queue=deque()
        
        rows = len(heights)
        cols=len(heights[0])
        
        row = 0
        for j in range(cols):
            pacific_queue.append((row,j))
            
        col = 0
        for j in range(1,rows):
            pacific_queue.append((j,col))
            
        row = rows-1
        for j in range(cols):
            atlantic_queue.append((row,j))
        
        col = cols-1
        for j in range(rows-1):
            atlantic_queue.append((j,col))
            
        """
        for i in range(rows):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, cols - 1))
        for i in range(cols):
            pacific_queue.append((0, i))
            atlantic_queue.append((rows - 1, i))
        
        """
        # print(pacific_queue, atlantic_queue)
        dir = [[1,0],[0,1],[-1,0],[0,-1]]
        def bfs(queue):
            visited = set()
            while queue:
                r,c = queue.popleft()
                visited.add((r,c))
                for dr,dc in dir:
                    nr,nc= r+dr,c+dc
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and heights[nr][nc] >= heights[r][c]:#if the inner coordinates are >= the outer, then water can flow from inner to outer, hence add them to queue
                        queue.append((nr,nc))
            return visited
            
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        
        return list(pacific_reachable.intersection(atlantic_reachable))#common between pacific and atlantic is the answer
        
                