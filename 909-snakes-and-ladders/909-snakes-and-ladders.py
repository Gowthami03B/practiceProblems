class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        arr, target, queue, seen = [-1], len(board) ** 2, collections.deque(), set()
        queue.append((1,0))#to start from position 1
        #the board is in zig zag style, hence we convert/flatten the board
        for i, row in enumerate(board[::-1]): #go in reverse
            if i%2 == 0:#even rows, same
                arr += row
            else:
                arr += row[::-1]#odd rows -reverse
        print(arr)
        
        while queue:
            position, moves = queue.popleft()#position is position on board
            if arr[position] != -1:#it means there's a snake or ladder
                position = arr[position]
            if position == target:
                return moves
            
            # Get the next steps
            for step in range(1 ,7):#6 options
                nextStep = position + step
                if nextStep <= target and nextStep not in seen:
                    seen.add(nextStep)
                    queue.append((nextStep,moves + 1))
        return -1
                
            
       