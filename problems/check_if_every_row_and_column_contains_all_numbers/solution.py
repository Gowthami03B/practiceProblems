class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        nums = set(range(1, n + 1)) #set of 1 to n {1,2,3}
        print(nums)
        for row in matrix:#for each row
            print(row)
            if set(row) != nums:#if row != set, false
                return False
            
        for col in zip(*matrix):#for each col and we need transpose, zip returns a tuple
            print(col)
            if set(col) != nums:#we convert tuple to set so not an issue
                return False
        return True