class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = -(x**2 + y**2)
            elem = (dist, x, y)
            if len(heap) < k:
                heapq.heappush(heap, elem)
            else:
                heapq.heappushpop(heap, elem)
        return [(x, y) for (dist, x, y) in heap]
        
