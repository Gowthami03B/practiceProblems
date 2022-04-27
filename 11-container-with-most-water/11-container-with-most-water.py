class Solution:
    def maxArea(self, height: List[int]) -> int:
        i , j = 0, len(height) - 1
        maxvolume = float('-inf')
        while(i < j):
            maxvolume = max(maxvolume, min(height[i],height[j])* (j-i))
            if height[i] < height[j]:
                i += 1
            elif(height[i] >= height[j]):
                j -= 1
        return maxvolume
    
    #[1,2,3,4]