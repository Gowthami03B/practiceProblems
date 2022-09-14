class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Two pointers
        i , j = 0, len(height) - 1
        maxvolume = float('-inf')
        # We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines. Futher, we maintain a variable maxarea to store the maximum area obtained till now. At every step, we find out the area formed between them, update maxarea
        while(i < j):
            maxvolume = max(maxvolume, min(height[i],height[j])* (j-i))
            if height[i] < height[j]:#to maximize the area, we choose to keep the line with higher height
                i += 1
            elif(height[i] >= height[j]):
                j -= 1
        return maxvolume
    
    #[1,2,3,4]