class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        #basically track all rows, cols,diagonal, antidiagonal
        #space is O(N), we have rows and cols of n size
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0#when row == col
        self.anti_diagonal = 0# col = n - row -1 #need to remember this

    def move(self, row: int, col: int, player: int) -> int:#O(1)
        p = 1 if player == 1 else -1 #since only 2 players, player 1 = 1, player 2= -1
        
        self.rows[row] += p
        self.cols[col] += p
        
        if row == col:
            self.diagonal += p
        
        if row + col == self.n - 1:
            self.anti_diagonal += p
        #we will have both pos and neg hence we take abs
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diagonal) == self.n or abs(self.anti_diagonal) == self.n:
            return player
        
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)