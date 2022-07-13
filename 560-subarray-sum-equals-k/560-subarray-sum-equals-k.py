class Solution:
    #bruteforce - O(N2), O(1)
    def subarraySum1(self, nums: List[int], k: int) -> int:
        count = 0
        if k in nums:
            count += nums.count(k)
            
        for i in range(len(nums)):
            sum = nums[i]
            for j in range(i+1, len(nums)):
                sum += nums[j]
                if sum == k:
                    count += 1
        return count
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        # First of all, the basic idea behind this code is that, whenever sums has increased by a value of k, we've found a subarray of sums=k.
#         Example: Let's say our elements are [1,2,1,3] and k = 3.
# and our corresponding running sums = [1,3,4,7]
# Now, if you notice the running sums array, from 1->4, there is increase of k and from 4->7, there is an increase of k. So, we've found 2 subarrays of sums=k.
#but there is also a subarray [3] that also needs to be in final array, hence we also check if csum - k in map, if so increment res
        count=defaultdict(int)
        csum=0
        res=0
        for n in nums:
            csum += n#csum =  1,3,4,7
            if csum==k:   #when csum == 3; res + 1
                res+=1
            if csum-k in count:#when csum =4, 7, csum-k in map, hence res + 1 
                res+=count[csum-k]
            
            count[csum] += 1#count - 1:1, 3:1, 4:1,7:1

        return res