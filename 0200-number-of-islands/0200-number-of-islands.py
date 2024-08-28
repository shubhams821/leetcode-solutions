class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visit = set()

        def bfs(i,j):
            q = collections.deque()
            visit.add((i,j))
            q.append([i,j])
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    directions = [[1,0],[0,1],[-1,0],[0,-1]]
                    for dr, dc in directions:
                        r, c= row+dr, col+dc
                        if r in range(Rows) and c in range(Cols) and (r,c) not in visit and grid[r][c] =="1":
                            bfs(r,c)
        island = 0
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] =="1" and (r,c) not in visit:
                    bfs(r,c)
                    island+=1
        return island
        
            
