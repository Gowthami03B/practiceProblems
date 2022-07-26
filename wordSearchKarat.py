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
def wordSearchKarat(grid, word):
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


grid = [
[ 'c', 't', 'n', 'a', 'x'],
[ 'c', 'c', 'a', 't', 'n'],
[ 'c', 'a', 'b', 'g', 'c'],
[ 'c', 't', 'e', 'e', 'c'],
[ 'd', 'h', 'n', 'g', 's'],
]
word = "cccab"
print(wordSearchKarat(grid, word))
