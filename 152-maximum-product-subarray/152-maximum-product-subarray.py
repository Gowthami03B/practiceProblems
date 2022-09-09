class Solution:
    def maxProductBruteForce(self, nums: List[int]) -> int:
        maxProd = max(nums) #single element can also be the largest product
        for i in range(len(nums)):
            currProd = nums[i]
            for j in range(i+1, len(nums)):
                currProd *= nums[j]
                maxProd= max(maxProd, currProd)
                if currProd == 0: #if prod is 0, there's no sense in going forward, we can start at the next index after 0
                    break
        return maxProd
    
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        min_so_far, max_so_far = nums[0], nums[0]
        result = max_so_far
        for i in range(1,len(nums)):
            currProd = nums[i]
            temp_max = max(currProd, max_so_far*currProd, min_so_far*currProd)#if we directly have max_so_far here, then this value would be used in min_so_far calculation
            min_so_far = min(currProd, max_so_far*currProd, min_so_far*currProd)
            max_so_far = temp_max
            print(max_so_far,min_so_far)
            result = max(max_so_far,result)
        return result
    
  