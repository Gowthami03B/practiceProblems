class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows, cols = [0] * n, [0] * n #list of 3, for each of 3 rows, cols
        diag = anti_diag = 0#maintaining 2 diagonals
        player = 1#player A is 1 and B is -1, makes it easier to track who wins
        for r,c in moves:
            rows[r] += player#for every r,c we update in rows and cols
            cols[c] += player
            if r == c:#if r==c, then the move is on diagonal
                diag += player
            if r + c == n-1:#this is tricky, anti diagonal is the 2 diagonal-[0,2],[1,1],[2,0], r + c == n-1
                anti_diag += player
            #basically we are accumulating points for each player
            #player A - 3, player B - -3
            #after we add points, we check if any row,col or diag has 3 points
            if any(abs(line) == n for line in (rows[r],cols[c],diag,anti_diag)):
                return "A" if player == 1 else "B"
            player *= -1#next turn is next player's
        return "Draw" if len(moves) == n * n else "Pending" #draw and no res when all moves are made, pending when more moves can be made