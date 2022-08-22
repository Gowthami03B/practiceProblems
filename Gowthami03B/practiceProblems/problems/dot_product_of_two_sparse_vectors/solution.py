class SparseVector:
    def __init__(self, nums: List[int]):
        # self.vector = nums
        self.nonzeros = defaultdict(int)
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n
                
        """
        approach 3 - using list of (index,val pairs)
        self.pairs = []
        for i, n in enumerate(nums):
            if n != 0:
                self.pairs.append([i,n])
        """

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
        if len(vec.nonzeros) < len(self.nonzeros):
            self.nonzeros, vec.nonzeros = vec.nonzeros, self.nonzeros
        for idx, val in self.nonzeros.items():#O(N)-hashmap, O(L)-dotproduct, O(L)-hashmap
            if idx in vec.nonzeros:
                totsum += val * vec.nonzeros[idx]
        return totsum
    
        """
        approach 3 - using list of (index,val pairs)
        O(N) - to create index,val pairs, O(L1)+O(L2) -FOR DOT PRODUCT
        v1 ,v2 =0,0
        totsum = 0
        while v1 < len(self.pairs) and v2 < len(vec.pairs):
            if self.pairs[v1][0] == vec.pairs[v2][0]:
                totsum += self.pairs[v1][1] * vec.pairs[v2][1]
                v1 += 1
                v2 += 1
            elif self.pairs[v1][0] < vec.pairs[v2][0]:
                v1 += 1
            else:
                v2 += 1
        return totsum
        """

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)