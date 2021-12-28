class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        rows, cols = len(rooms), len(rooms[0])
        q = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if(rooms[r][c] == 0):
                    q.append([r,c])
                    visit.add((r,c))

        def addRoom(r,c):
            if(r < 0 or r == rows or c < 0 or c == cols or (r,c) in visit or rooms[r][c] == -1):
                return
            visit.add((r,c))
            q.append([r,c])

        dist = 0
        while q:
            n = len
            for i in range(len(q)):
                r,c = q.popleft()
                addRoom(r + 1, c)
                addRoom(r , c + 1)
                addRoom(r - 1, c)
                addRoom(r , c - 1)
                rooms[r][c] = dist
            dist+=1  
        