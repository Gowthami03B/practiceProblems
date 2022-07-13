class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        curr_color = image[sr][sc]
        queue = deque()
        visited = set()
        dir = [[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(rows):
            for j in range(cols):
                if i == sr and j == sc:
                    image[i][j] = newColor
                    queue.append((i,j))
                    visited.add((i,j))
        while(queue):
            r,c = queue.popleft()
            for dr,dc in dir:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and image[nr][nc] == curr_color and (nr,nc) not in visited:
                    image[nr][nc] = newColor
                    queue.append((nr,nc))
                    visited.add((nr,nc))
        return image
                    