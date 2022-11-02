class Solution:
    #DP
    def trap1(self, height: List[int]) -> int:
        left_heights = []
        right_heights = []
        n = len(height)
        max_left = max_right = 0
        rain_units = 0
        for i in range(len(height)):
            max_left = max(height[i],max_left)
            left_heights.append(max_left)
            max_right = max(height[n - i - 1],max_right)
            right_heights.append(max_right)
        # print(left_heights,right_heights)
        right_heights.reverse()
        for i in range(len(height)):
            rain_units += (min(left_heights[i],right_heights[i]) - height[i])
                                                                        
        return rain_units
    
    def trap(self, height: List[int]) -> int:
        left,right = 0, len(height) - 1
        max_left = max_right = 0
        rain_units = 0
        while left <= right:
            if height[left] <= height[right]:
                max_left = max(height[left],max_left)
                rain_units += max_left - height[left]
                left += 1
            else:
                max_right = max(height[right],max_right)
                rain_units += max_right - height[right]
                right -= 1
        return rain_units

                