from collections import defaultdict
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        map = defaultdict(int)
        res = set()
        if m > n:
            for i in range(m):
                map[nums1[i]] += 1
            for i in range(n):
                if map[nums2[i]]:
                    res.add(nums2[i])
        else:
            for i in range(n):
                map[nums2[i]] += 1
            for i in range(m):
                if map[nums1[i]]:
                    res.add(nums1[i])
        return list(res)
        
        