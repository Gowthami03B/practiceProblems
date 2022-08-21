class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            dist = math.sqrt(x*x + y*y)
            heappush(heap, (-dist, [x,y]))
            if len(heap) > k:
                heappop(heap)
        return [heappop(heap)[1] for i in range(len(heap))]
