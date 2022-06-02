class Solution:
    def search1(self, nums: List[int], target: int) -> int:
        """
        [4,5,6,7,0,1,2] - rotate index is at 4 to push 4,5,6,7 towards the end
        once we find rotate index, we can check if rotate index
        
        [4,0,1,2,3] nums[pivot] 1 < 4 nums[left], search space left, right = pivot + 1,
        we need to compare 4 and 0 so we know pivot point
        """
        def find_rotate_index(left, right):
            if nums[left] < nums[right]: #left = 0, right = len(nums)-1 if left < right, then array isn't rotated
                return 0
            while left <= right:
                pivot = (left+right)//2
                if nums[pivot] > nums[pivot+1]: #[4,5,6,7,1,2]; 7 > 1, rotated at 1
                    return pivot + 1
                else:
                    if nums[pivot] > nums[left]:#[4,5,6,7,8,1,2]; check if mid > start(means its the rotated part), search space is right side, else left
                        left = pivot + 1
                    else:
                        right = pivot - 1
            
        def search(left,right):    
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            return -1
                    
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        index = find_rotate_index(0, n-1)
        if nums[index] == target:
            return index
        if index == 0:#if index is 0, array is already sorted, hence search from start to end
            return search(0,n-1)
        if nums[0] < target:#[4,5,6,7,1,2,3] target=2; index = 4 if start > target(means element is in non rotated part): search is right side
            #[4,5,6,7,8,1,2]  target=5; index = 4 and start < target means target is in nonrotated part, search is left side
            return search(0, index)
        return search(index,n-1)

    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]: #example [4,5,6,1,2,3], and say target = 5
                #6>4, hence if target > start and target < mid - search left else right
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else: #example [4,5,1,2,3], and say target = 2
                #1<4, hence if target < end and target > mid - search right else left
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1