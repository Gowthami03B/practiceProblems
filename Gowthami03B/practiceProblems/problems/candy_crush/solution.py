class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # Edge case
        if board is None:
            return board
        
        ROWS, COLS = len(board), len(board[0])
        is_all_crushed = True
        
        # Step 1: Tag rows that need to be crushed
        # We are going to achieve this by searching each row with a sliding window of 3 
        # and if we find numbers that match, we will keep track of it. We will mark it 
        # negative so we know which values to crush and because there's a chance of a vertical crush that depends on our horizontal crush
        for r in range(ROWS):
            for c in range(COLS - 2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])
                    is_all_crushed = False
            
        
        # Step 2: Tag columns that need to be crushed
        # We are going to achieve this by searching each column with a sliding window
        # of 3 and if we find numbers that match, we will keep track of it. We will mark it negative so we know which values to crush
        for c in range(COLS):
            for r in range(ROWS - 2):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                    is_all_crushed = False
        
        # Step 3: Crush the candies
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] < 0:
                    board[row][col] = 0
        # print(board)
        # Step 4: Gravity
        # For every column, we want to put every positive number at the bottom.
        # For every positive number, we want to swap it so that positive
        # number are at the bottom and zeroes are at the top. It is 
        # similar to https://leetcode.com/problems/move-zeroes/
        for col in range(COLS):
            idx = ROWS - 1
            for row in range(ROWS - 1, -1, -1):
                if board[row][col] > 0:
                    board[idx][col], board[row][col] = board[row][col], board[idx][col]
                    idx -= 1
        
        return board if is_all_crushed else self.candyCrush(board)

# Time Complexity: O(m * n) since we have to iterate through the whole board a couple times

# Space Complexity: O(1)
