class Solution:
    def minSwaps(self, data: List[int]) -> int:
        #to find the number of swaps, if we can find the max number of ones in a particular window (1,1,0,0), then total ones say 4, then ones - max ones is the number of swaps (2 0's will be awapped by 2one's)
        ones = sum(data) #total ones is the window length we are looking at
        cnt_one = max_one = 0#max_ones in a window size

        #We will use two pointers left and right to maintain a sliding window of length ones, and while we check every window of the input array data, we would calculate the number of 1's in it as cnt_one and store the largest one as max_one.
        #we update the window when the current window has length > ones by deducting left boundary
        left = right = 0
        while right < len(data):
            cnt_one += data[right]
            right += 1
            # when the window length is > no of ones
            # remove the leftmost one
            if right - left > ones:
                cnt_one -= data[left]
                left += 1
            max_one = max(max_one, cnt_one)#max ones in a window of length ones
        return ones - max_one#if we can find the max number of ones in a particular window, then total ones - max ones is the number of swaps
       