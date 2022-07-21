class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
         # To find all heights and widths, we must first sort our inputs horizontalCuts and verticalCuts. This will ensure that all of the cuts that are beside each other on the cake are also beside each other in the array.
        horizontalCuts.sort()
        verticalCuts.sort()
        #if we cut horizontally width wise, then max height is the diff between cuts but width is w
        #if we cut vertically, then max height is h and max width is diff between cuts
    
        maxHeight = max(horizontalCuts[0], h - horizontalCuts[-1])#but for edges, say [1],h=5,w=4; when you make 1 cut horizontally, max height is (1, 5-1 i.e 4) 4
        #say [1,3] - maxHeight is 1, 5-3 i.e 2
        print(maxHeight)
        for i in range(1, len(horizontalCuts)):
            maxHeight = max(maxHeight, horizontalCuts[i] - horizontalCuts[i-1])#hence diff between 2 adjacent cuts, is the maxHeight for horizontal cuts
        
        maxWidth = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            maxWidth = max(maxWidth, verticalCuts[i] - verticalCuts[i-1])
            
        return (maxHeight*maxWidth)%(10**9 + 7) #to prevent integer overflow, all numbers less than this will result in the same number as output