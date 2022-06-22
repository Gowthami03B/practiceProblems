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
        for n1 in nums1:
            for n2 in nums2:
                if len(heap) < k:
                    heappush(heap, (-n1-n2, [n1,n2]))
                else:
                    if heap and -heap[0][0] > n1+n2:
                        heappop(heap)
                        heappush(heap, (-n1-n2, [n1,n2]))
                    else:
                        break
        
        return [heappop(heap)[1] for _ in range(k) if heap]