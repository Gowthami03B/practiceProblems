class Solution:
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        res = []
        smallerarr_map = defaultdict(int)
        if m > n:
            nums1,nums2 = nums2,nums1#smaller array in nums1
        
        for num in nums1:
            smallerarr_map[num] += 1
        for num in nums2:
            if num in smallerarr_map and smallerarr_map[num] > 0:
                res.append(num)
                smallerarr_map[num] -=1
        return res
        
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i,j = 0,0
        res = []
        while(i < len(nums1) and j < len(nums2)):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i +=1
                j +=1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res
            
                
        