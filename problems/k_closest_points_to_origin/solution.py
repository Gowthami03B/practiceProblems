class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        output = []
        for point in points:
            x, y = point
            dist = math.sqrt(x*x + y*y)
            heappush(heap, (-dist, x,y))
            if len(heap) > k:
                heappop(heap)
        for dist,x,y in heap:
            output.append([x,y])
        return output