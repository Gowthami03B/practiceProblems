class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lowerbound = self.findBound(nums, target, True)
        if lowerbound == -1:
            return [-1,-1]
        upperbound = self.findBound(nums, target, False)
        return [lowerbound, upperbound]
    
    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right)//2
            if(target == nums[mid]):            
                    if isFirst:
                        if(mid == left or nums[mid - 1] < target):
                            return mid
                        right = mid - 1
                    else:
                        if(mid == right or nums[mid+1] > target):
                            return mid
                        left = mid + 1
            elif(target > nums[mid]):
                left = mid + 1
            else:
                right = mid - 1
        return -1
            
        