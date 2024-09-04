class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visit = set()
        perim =[0]
        def bfs(i,j):
            q = collections.deque()
            q.append([i,j])
            visit.add((i,j))
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    directions =[[1,0],[0,1],[-1,0],[0,-1]]
                    for dr, dc in directions:
                        r, c = row+dr, col +dc
                        if r in range( Rows) and c in range(Cols) and (r,c) not in visit and grid[r][c]:
                            q.append([r,c])
                            visit.add((r,c))
                        if r not in range(Rows) or c not in range(Cols) or not grid[r][c]:
                            perim[0]+=1
        for r in range(Rows):
            for c in range(Cols):
                if (r,c) not in visit and grid[r][c]:
                    bfs(r,c)
        return perim[0]