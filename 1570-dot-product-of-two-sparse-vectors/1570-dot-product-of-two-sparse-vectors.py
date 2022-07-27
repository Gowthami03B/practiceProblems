class SparseVector:
    def __init__(self, nums: List[int]):
        # self.vector = nums
        self.nonzeros = defaultdict(int)
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        #O(N) = for creating the tuples and dot product, O(1) using zip
        # v2 = vec.vector #vec.vector is the 2nd vectors object, bcs v1.dotproduct(v2)
        # v1 = self.vector#has 1st vector's obj
        # totsum = 0
        # for x,y in zip(v1,v2):
        #     totsum += x * y
        # return totsum
        totsum = 0
        for idx, val in self.nonzeros.items():#O(N)-hashmap, O(L)-dotproduct, O(L)-hashmap
            if idx in vec.nonzeros:
                totsum += val * vec.nonzeros[idx]
        return totsum

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)