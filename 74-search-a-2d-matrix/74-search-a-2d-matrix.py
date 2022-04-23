class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        collen, i = len(matrix[0]), -1
        if len(matrix) == 0:
            return False
        if matrix[0][0] > target:
            return False
        elif matrix[0][0] == target:
            return True
        if len(matrix) == 1:
            i = 0
        else:
            i = self.findRow(matrix, target)
        if i >= 0:        
            s , h = 0,collen - 1
            while(s <=h):
                mid = (s+h)//2
                if(matrix[i][mid] == target):
                    return True
                elif(matrix[i][mid] < target):
                    s = mid + 1
                else:
                    h = mid - 1
        return False
    
    def findRow(self,matrix : List[List[int]], target:int) -> int:
        for i in range(0,len(matrix)):
            if i < len(matrix)-1:
                if matrix[i][0] < target and matrix[i+1][0] > target:
                    return i
                elif matrix[i][0] == target:
                    return i
                elif matrix[i+1][0] == target:
                    return i+1
            else:
                return i
        return -1
            