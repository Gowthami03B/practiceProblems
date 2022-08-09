class Solution:
    def findDuplicateModified(self, nums: List[int]) -> int:
        #we modified the nums
        #In Python, the sort() function is implemented using the Timsort algorithm, which has a worst-case space complexity of O(n)
        if len(nums) == 0:
            return -1
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
            
    #map each number to its equivalent index in the array. For instance, map the number 5 to index 5 (i.e. nums[5] = nums[5]=5). Since there are (n + 1) positions/indexes in the input array, and the numbers range from 1 to n, at least one index will have more than one number 
    """
    To illustrate the algorithm, let's consider an example [3,3,5,4,1,3]
store(nums, 0)store(nums,0)

Here cur = 0 and nums[cur] = 3
Back up the number 3 (that's at index 0)
Store 0 at index 0. The array is now: [0,3,5,4,1,3]
Recursively call store(nums, 3), next step would be store(nums,4), store(nums,1), store(nums,3) but 3 is already at nums[3], hence repetitive
"""
    def findDuplicateSpace(self, nums: List[int]) -> int:
        def store(nums, curr=0):
            if curr == nums[curr]:
                return curr
            temp = nums[curr]
            nums[curr] = curr#storing currth val at currth index
            return store(nums, temp)
        
        return store(nums)
    
    def findDuplicateSwap(self, nums: List[int]) -> int:
        #similar to above where we start with putting the first value in it's index position (swap), then repeat until nums[0] != nums[nums[0]], if they are equal that's the duplicate
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]
    
    def findDuplicate(self, nums: List[int]) -> int:
        #Consider an array that has n distinct numbers in the range [1,n]. For example: [1,2,3,4,5]. If we pick any one of these 5 numbers and count how many numbers are less than or equal to it, the answer will be equal to that number. So in [1,2,3,4,5], if you pick the number 4, there's exactly 4 numbers that are less than or equal to 4.
        #[3,3,5,4,1,3], counts =[1,1,4,5,6]
        #Binary search is log n but for each search, we need to count utmost n values hence O(n log n)
        low,high = 0,len(nums) - 1
        while(low <= high):
            mid = low + (high-low)//2 #here 4 becomes mid first
            count = 0
            # Count how many numbers are less than or equal to 'mid'
            count = sum(num <= mid for num in nums)
            if count >mid:
                duplicate= mid#duplicate would be 4 as count > mid, but is not the duplicate, we need to lessen the search space
                high = mid - 1
            else:
                low = mid + 1
        return duplicate