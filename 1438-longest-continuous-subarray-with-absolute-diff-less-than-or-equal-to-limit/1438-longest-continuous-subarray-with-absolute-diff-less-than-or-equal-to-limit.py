class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        incQ =deque() #stores the min elements in a subarray
        decQ=deque()#stores max element in a subarray
        i = 0
        for num in nums:
            while incQ and incQ[-1] > num:#if current min is > num, pop bcs we need to push the new min
                incQ.pop()
            while decQ and decQ[-1] < num:#if current max is < num, pop bcs we need to push the new max
                decQ.pop()
            incQ.append(num)
            decQ.append(num)
            if decQ[0] - incQ[0] > limit:#diff between min and max > limit
                # print(incQ, decQ)
                # deque([2]) deque([8, 2])
# deque([2, 4, 7]) deque([7])
                #i is the start position
                if incQ[0] == nums[i]: incQ.popleft()#if inc[0]==nums[i],pop that else pop dec
                if decQ[0] == nums[i]: decQ.popleft()
                i +=1 #increment start and slide the subarray
        return len(nums) - i#return end-start i.e len(nums-i)
        