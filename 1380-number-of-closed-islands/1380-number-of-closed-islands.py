class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visit = set()

        def bfs(i,j):
            q = collections.deque()
            q.append([i,j])
            visit.add((i,j))
            flag = False
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    directions =[[1,0],[0,1],[-1,0],[0,-1]]
                    for dr, dc in directions:
                        r,c = row+dr, col+dc
                        if r in range(Rows) and c in range(Cols) and (r,c) not in visit and not grid[r][c]:
                            q.append([r,c])
                            visit.add((r,c))
                        if r not in range(Rows) or c not in range(Cols):
                            flag = True
            return 1 if not flag else 0
        
        island = 0
        for r in range(Rows):
            for c in range(Cols):
                if not grid[r][c] and (r,c) not in visit:
                    island += bfs(r,c)
        return island