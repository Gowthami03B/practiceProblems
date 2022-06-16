class Solution:
    def maxSlidingWindowBruteForce(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]
        res = []
        # for i in range(len(nums)-k+1):
        #     res.append(max(nums[i:i+k]))
        return [max(nums[i:i+k]) for i in range(len(nums - k + 1))]
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue, n, res = deque(), len(nums), []
        for i in range(n): 
            # maintain the monotonic decreasing queue
            while queue and queue[-1] < nums[i]: #if last element < curr, we don't need any of elements in queue as they cannot be the maximum
                queue.pop() 
            queue.append(nums[i]) #if the condition fails, we just append
            
            #i >= k-1 after finishing first window and every subsequent window, we can start appending the start of queue to res
            if i >= k - 1:
                res.append(queue[0])
            # if the max in the queue(first position) is no longer in the current window, pop it out
                if queue[0] == nums[i - k + 1]: 
                    queue.popleft()
        return res