class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # res = [0] * len(nums)
        # if len(nums) == 1:
        #     return [nums[0] * nums[0]]
        # idx = len(nums) - 1
        # i,j = 0,len(nums)-1
        # while(i <= j):
        #     if abs(nums[i]) > abs(nums[j]):
        #         res[idx] = nums[i] * nums[i]
        #         i += 1
        #     else:
        #         res[idx] = nums[j] * nums[j]
        #         j -= 1
        #     idx -= 1
        # return res
        
        #merge sort - also uses extra space, we find end of negative numer index, then loop thru arrays from k-1 to 0 and k to n-1, since neg array hence loop start to end
        #start idx at 0 for main array to add data
        n = len(nums)
        if n == 1:
            return [nums[0] * nums[0]]
        for k in range(n):
            if nums[k] < 0:
                continue
            else:
                break
        temp = [0] * n
        #0 to k-1 - neg number, k to n-1 positive number
        i , j , idx = k-1,k, 0
        while(j < n and i >= 0):
            if((nums[i] * nums[i]) < (nums[j] * nums[j])):
                temp[idx] = nums[i] * nums[i] 
                i -= 1
            else:
                temp[idx] = nums[j] * nums[j] 
                j += 1
            idx += 1
        while(i >= 0):
            temp[idx] = nums[i] * nums[i] 
            i -= 1
            idx += 1
        while(j < n):
            temp[idx] = nums[j] * nums[j] 
            j += 1
            idx += 1
        return temp