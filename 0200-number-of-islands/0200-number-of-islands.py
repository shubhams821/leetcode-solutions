class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        island = 0
        visit = set()
        Rows, Cols = len(grid), len(grid[0])
        def bfs(i,j):
            q = collections.deque()
            q.append([i,j])
            visit.add((i,j))
            while q:
                row, col = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for dr, dc in directions:
                    r,c = row+dr, col + dc
                    if (r in range(Rows) and 
                        c in range(Cols) and
                        grid[r][c] == "1" and
                        (r,c) not in visit):
                        q.append([r,c])
                        visit.add((r,c))
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    island+=1
        return island