class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x,y in points:
            dist = x**2 + y**2
            minHeap.append([dist,x,y])
        heapq.heapify(minHeap)
        res = []
        while k>0:
            dist,x,y = heapq.heappop(minHeap)
            k-=1
            res.append([x,y])
        return res
