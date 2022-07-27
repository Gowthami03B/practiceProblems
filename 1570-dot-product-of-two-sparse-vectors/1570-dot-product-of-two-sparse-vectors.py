class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        v2 = vec.vector
        v1 = self.vector
        totsum = 0
        for x,y in zip(v1,v2):
            totsum += x * y
        return totsum

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)