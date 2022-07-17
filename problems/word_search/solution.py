class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()
        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        
        def dfs(r,c,index):
            if index == len(word):#we pass index + 1 everytime and if it == len(word), we reached end of word and there's a match
                return True
            if r < 0 or r == rows or c < 0 or c == cols or (r,c) in path or board[r][c] != word[index]:
                return False
            
            path.add((r,c))#add to path
            for r1,c1 in dir: 
                if dfs(r+r1, c+c1, index + 1):#search in all 4 directions
            #basically we keep going if we find a match and will be returning false for wrong directions, and only if it returns True after reaching end of the word, we return true from here and keep returning true recursively to the top of the stack
                    return True
            path.remove((r,c)) #[["C","A","A"],["A","A","A"],["B","C","D"]]
#"AAB", we need remove to backtrack and remove a path when we can't proceed anymore
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i,j,0): #start dfs once the 1st letter matches and if it's found return true
                        return True
        return False