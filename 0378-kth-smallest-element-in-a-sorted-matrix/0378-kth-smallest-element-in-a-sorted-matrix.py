class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        Rows, Cols = len(matrix), len(matrix[0])
        minHeap = []

        for i in range(Rows):
            heapq.heappush(minHeap, (matrix[i][0], i,0))
        
        while k >0:
            elem, r,c = heapq.heappop(minHeap)
            try:
                heapq.heappush(minHeap, (matrix[r][c+1], r, c+1))
            except:
                pass
            k-=1
        return elem