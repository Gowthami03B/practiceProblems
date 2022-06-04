class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i,j = 0,0
        while(i < len(nums1) and j < len(nums2)):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        while(i < len(nums1)):
            nums.append(nums1[i])
            i+= 1

        while(j < len(nums2)):
            nums.append(nums2[j])
            j+= 1

        print(nums,i,j)
        mergedArrayLen = len(nums)
        if mergedArrayLen % 2 ==1:
            return nums[mergedArrayLen//2]
        else:
            return (nums[mergedArrayLen//2] + nums[mergedArrayLen//2 - 1])/2