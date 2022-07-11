class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = [set() for _ in range(n)]#create hashsets for all 9 rows, 9 cols and 9 boxes
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]
        for r in range(n):
            for c in range(n):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r]:#if we already saw the number in the current row, return False
                    return False
                rows[r].add(val)
                
                if val in cols[c]:
                    return False
                cols[c].add(val)
                
                idx = (r // 3) * 3 + c // 3#tricky logic, need to arrive at this formula by seeing what all row and col values are part of the same box
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)
        return True