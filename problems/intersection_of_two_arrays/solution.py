from collections import defaultdict
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #idea is same, loop over the small list to find match in big list
        #but multiple data structures - can simplify the approach
        #O(N+M), O(N or M(whichever is largest))
#         m = len(nums1)
#         n = len(nums2)
#         map = defaultdict(int)
#         res = set()
#         if m > n:
#             for i in range(m):
#                 map[nums1[i]] += 1
#             for i in range(n):
#                 if nums2[i] in map:
#                     res.add(nums2[i])
#         else:
#             for i in range(n):
#                 map[nums2[i]] += 1
#             for i in range(m):
#                 if nums1[i] in map:
#                     res.add(nums1[i])
#         return list(res)
    
#         #approach 2
#         #In Python it's intersection operator, in Java - retainAll() function.
#         #time complexity - for intersection O(N+M)
#         #space complexity - O(N+M) when all elements are different
#         set1 = set(nums1)
#         set2 = set(nums2)
#         return list(set1 & set2)
    
        #approach 3
        #The idea is to convert both arrays into sets, and then iterate over the smallest set checking the presence of each element in the larger set.
        #time complexity - O(N+M), O(N) time taken to convert nums1 to set,O(M) time taken to convert nums2 to set
        #space complexity - O(N+M) when all elements are different
        set1 = set(nums1)
        set2 = set(nums2)
        res = []
        if len(set1) < len(set2):
            for i in set1:
                if i in set2:
                    res.append(i)
        else:
            for i in set2:
                if i in set1:
                    res.append(i)
        return res
        
        
        
        