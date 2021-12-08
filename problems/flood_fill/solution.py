class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image == None:
            return 
        oldColor = image[sr][sc]
        height = len(image)
        width = len(image[1])

        def dfs(sr,sc):
            if 0 <= sr < height and 0 <= sc < width and image[sr][sc] == oldColor and image[sr][sc] != newColor:
                image[sr][sc] = newColor
                dfs(sr+1, sc)
                dfs(sr-1,sc)
                dfs(sr, sc+1)
                dfs(sr, sc-1)
            
        dfs(sr,sc)
        return image
        