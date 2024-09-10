class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])

        minHeap = [(grid[0][0],0,0)]
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visit = set()
        while minHeap:
            tmp, r,c = heapq.heappop(minHeap)
            if (r,c) == (Rows-1, Cols-1):
                return tmp
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr in range(Rows) and nc in range(Cols) and (nr,nc) not in visit:
                    heapq.heappush(minHeap,(max(grid[nr][nc],tmp),nr,nc))
                    visit.add((nr,nc))