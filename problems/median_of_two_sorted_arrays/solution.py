class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        #an array of size 13, can be partitioned as 2 around the middle element
        #so basically we need to know the bounds of our left partition.
        A = [1,2,2,4]B =  [2,3,3,5,7,8,9]
        [1,2,2,2,3,3,4,5,7,8,9] #last 3 is the mid element
        [1,2] [2,3,3] 5 <= 2; False
        [1,2,2] [2,3] 3<= 4 and 4 <= 5 - mid is min(3,4)
        
        A = [1,2,2,3] B = [2,4,5,7,8,9]
        [1,2] [2,4,5] (left partition 5) but 5<=2 false expand A's mid
        [1,2,2] [2,4] but 5<=3 false expand A's mid
        [1,2,2,3] [2] 4 <infinity 
        mid is the max of left + min of right /2 i.e 3+4/2
        [1,2,2,2,3,4,5,7,8,9] #max of right partition 
        """
        A,B = nums1, nums2
        m,n = len(nums1),len(nums2)
        totLen = m + n
        
        #binary search on smaller array
        if n < m:
            A,B = B,A
        l , r = 0, len(A) - 1
        while True:
            mid = (l + r)//2
            j = (totLen//2) - mid - 2 #say total 13, 6 elements 1 half, mid of A is 1 (means 0 and 1 indices, 2 elements), 4 elements in B from 0,1,2,3 hence 6 - 1 - 2
            #Aleft, Bleft are neg inf, and rights are inf, hence output can never be inf as we choose the max(lefts) and min(rights)
            Aleft = A[mid] if mid >= 0 else float('-inf')  #it will be out of bound is mid < 0
            Bleft = B[j] if j >= 0 else float('-inf') 
            Aright = A[mid + 1] if (mid + 1) < len(A) else float('inf')#it will be out of bound is mid+1 > len(A)
            Bright = B[j+1] if (j + 1) < len(B) else float('inf')
            
            #if left partition is as expected
            if Aleft <= Bright and Bleft <= Aright:
                if totLen % 2: #odd len, element is always on right side and min of right
                    return min(Aright, Bright) 
                else:#even len, so its last ele in left and 1st ele in right ie max of lefts, min of rights
                    return (max(Aleft, Bleft) + min(Aright , Bright))/2
            elif Bleft > Aright:#expand left partition in A, to increase Aright
                l = mid + 1
            else:#else shrink left
                r = mid - 1
    
    #with space, use merge sort technique
    def findMedianSortedArraysMergeSort(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i,j = 0,0
        #check if nums1 < nums2, then update nums accordingly
        while(i < len(nums1) and j < len(nums2)):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        #fill the remaining elements from both arrays in nums
        while(i < len(nums1)):
            nums.append(nums1[i])
            i+= 1

        while(j < len(nums2)):
            nums.append(nums2[j])
            j+= 1

        print(nums,i,j)
        mergedArrayLen = len(nums)
        #len / 2 is the median of the odd length array and if it is even, average of len / 2th and len / 2 – 1
        if mergedArrayLen % 2 ==1:
            return nums[mergedArrayLen//2]
        else:
            return (nums[mergedArrayLen//2] + nums[mergedArrayLen//2 - 1])/2