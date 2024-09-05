class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visit = set()
        res = 0
        def bfs(i,j):
            q = collections.deque()
            q.append([i,j])
            visit.add((i,j))
            area = 1
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    directions = [[1,0],[0,1],[-1,0],[0,-1]]
                    for dr, dc in directions:
                        r,c = row+dr, col+dc
                        if r in range(Rows) and c in range(Cols) and grid[r][c] and (r,c) not in visit:
                            q.append([r,c])
                            visit.add((r,c))
                            area +=1
            return area
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] and (r,c) not in visit:
                    res = max(res, bfs(r,c))
        return res 