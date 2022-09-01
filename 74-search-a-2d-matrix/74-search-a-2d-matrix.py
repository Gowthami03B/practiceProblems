class Solution:
    #I am finding the row which can possibly have the element and then doing a binary search
#     def searchMatrixMethod1(self, matrix: List[List[int]], target: int) -> bool:
#         collen, i = len(matrix[0]), -1
#         if len(matrix) == 0:#when len ==0
#             return False
#         if matrix[0][0] > target:#start element < target, else target doesn't exist
#             return False
#         elif matrix[0][0] == target:
#             return True
#         if len(matrix) == 1: #if only one row, then that row
#             i = 0
#         else:
#             i = self.findRow(matrix, target)
#         if i >= 0:        
#             s , h = 0,collen - 1
#             while(s <=h):
#                 mid = (s+h)//2
#                 if(matrix[i][mid] == target):
#                     return True
#                 elif(matrix[i][mid] < target):
#                     s = mid + 1
#                 else:
#                     h = mid - 1
#         return False
    
#     def findRow(self,matrix : List[List[int]], target:int) -> int:
#         for i in range(0,len(matrix)):
#             if i < len(matrix)-1: 
#                 if matrix[i][0] < target and matrix[i+1][0] > target: #means we found possible row
#                     return i
#                 elif matrix[i][0] == target: #first element match
#                     return i
#                 elif matrix[i+1][0] == target:# #first element match in subsequent row
#                     return i+1
#             else:#loop doesn't reach last row, hence another condition to return last row
#                 return i
#         return -1
    
    #if this was a n*n matrix, we could just do j-=1 if num > target and row += 1 if num < target, where row =0 to n and col= n to 0
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowlen , collen = len(matrix), len(matrix[0])
        if rowlen == 0:
            return False
        s,h = 0, rowlen*collen - 1
        while(s <= h):
            mid = (s+h)//2
            ele = matrix[mid//collen][mid%collen]#reminder from modulus is always in the range of 0..divisor, hence column len, else out of range
            if(ele == target):
                return True
            elif(ele < target):
                s = mid + 1
            else:
                h = mid - 1
        return False        