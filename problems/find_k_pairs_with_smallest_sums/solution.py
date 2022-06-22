from heapq import heappush, heappop
class Solution:
    def kSmallestPairsTLE(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        #Method 1
        output,res = [],[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                tempSum = nums1[i] + nums2[j]
                heappush(res, (tempSum, (nums1[i],nums2[j])))
        
        while(res):
            if len(output) == k:
                break
            output.append(heappop(res)[1])

        return output
    
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        output,heap = [],[]
        """
        n1 = [1,1,3] n2 = [1,2,2] k =2; we push (1,1), (1,2) first
        and since len > k and another (1,1) sum < (1,2) sum, the larger element must be popped 
        """
        for n1 in nums1:
            for n2 in nums2:
                if len(heap) < k:
                    heappush(heap, (-n1-n2, [n1,n2]))#keep pushing until length is k
                    #we need maxheap so the largest sum is at top
                else:#once len exceeded, see if heap top > curr sum, if so, pop larger element and push, else break
                    if heap and -heap[0][0] > n1+n2:
                        heappop(heap)
                        heappush(heap, (-n1-n2, [n1,n2]))
                    else:
                        break #most important, if for any n1, n2 if their sum is not smaller than top of heap, as the arrays are in sorted order, we won't find any sum smaller, hence we can break to stop there -n1 = [1,1,3] n2 = [1,2,2,4,5]
#without break, execution continue to 1,4 & 1,5 with break, that doesn't happen
        
        return [heappop(heap)[1] for _ in range(k) if heap]