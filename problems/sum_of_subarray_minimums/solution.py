class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        N = len(arr)
        ans = 0
        nextSmaller = [N]*N#to contain next smaller element's index
        #we initiate with N as it's the right side boundary and also we need it to count single subarray sums also 
        prevSmallerOrEqual = [-1]*N #array to contain the indices of the prev smaller element, we initiate with -1 as it's the left side boundary (no elements - -1)
        
        #construct nextSmaller [1]
        stack = []
        for i in range(N):
            n = arr[i]
            while stack and n<arr[stack[-1]]:#if n < last element on stack, pop
                nextSmaller[stack.pop()] = i#nextSmaller[popped element] = i#will have i as the next smaller element
            stack.append(i)
        #construct prevSmallerOrEqual
        stack = []
        for i in range(N-1, -1, -1):
            n = arr[i]
            while stack and n<=arr[stack[-1]]:
                prevSmallerOrEqual[stack.pop()] = i#same as above, reversed and tracks prev smaller element
            stack.append(i)
            
        #[4, 3, 3, 4, 5] [-1, 0, 1, 0, -1] for [11,81,94,43,3]
        
        #get ans
        for i in range(N):
            n = arr[i]
            r = nextSmaller[i]#this is the right boundary. so all subarrays from i to r have i as smaller
            l = prevSmallerOrEqual[i]#this is left boundary, so all subarrays from l to i have this as minimum
            ans += (i-l)*(r-i)*n #[0]#hence i-l * r-i * num
            
        return ans%(10**9+7)
    