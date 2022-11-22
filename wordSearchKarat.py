"""
Given a grid of characters and a word you have to return the coordinates if you can create the word from that grid. You can move only in right or down direction.
ex - grid = [
[ 'c', 't', 'n', 'a', 'x'],
[ 'c', 'c', 'a', 't', 'n'],
[ 'c', 'a', 'b', 'g', 'c'],
[ 'c', 't', 'e', 'e', 'c'],
[ 'd', 'h', 'n', 'g', 's'],
]
word = "cccc", output = [(0,0), (1,0), (2, 0), (3, 0)]
word = "cccab", output = [(0,0), (1,0), (2, 0), (2, 1), (2, 2)] or [(0,0), (1,0), (1, 1), (2, 1), (2, 2)]
"""
def wordSearchKarat1(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    res = []
    def dfs(row, col, index, path):
        if index == len(word):
            res.append(path)
            return True
        if row < 0 or row == rows or col <0  or col == cols or grid[row][col] != word[index]:
            return False
        if dfs(row+1, col, index + 1, path + [(row,col)]) or dfs(row, col + 1, index + 1, path +[(row,col)]):
            return True
    for i in range(rows):
        for j in range(cols):
            dfs(i,j,0,[])
    return res

def wordSearchKarat(grid,word):
    dir = [[0,1],[1,0]]
    rows = len(grid)
    cols = len(grid[0])
    coordinates = []
    def bfs(r,c,index):
        if index == len(word):
            return True
        if r <0  or c <0 or r==rows or c == cols or grid[r][c] != word[index]:
            return False
        coordinates.append((r,c))
        for dr,dc in dir:
            nr,nc = r+dr, c+dc
            if bfs(nr,nc,index+ 1):
                return True
        coordinates.pop()
        return False

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:
                if bfs(i,j,0):
                    return coordinates


grid = [
[ 'c', 't', 'n', 'a', 'x'],
[ 'c', 'c', 'a', 't', 'n'],
[ 'c', 'a', 'b', 'g', 'c'],
[ 'c', 't', 'e', 'e', 'c'],
[ 'd', 'h', 'n', 'g', 's'],
]
word = "cccab"
print(wordSearchKarat(grid, word))
