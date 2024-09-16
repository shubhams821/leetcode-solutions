class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visit = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(i,j):
            if i not in range(Rows) or j not in range(Cols) or (i,j) in visit or grid[i][j] ==0:
                return
            visit.add((i,j))
            for dr, dc in directions:
                dfs(i+dr, j+dc)
        
        def bfs():
            res, q = 0, deque(visit)

            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    print(row, col)
                    for dr, dc in directions:
                        r,c = row+dr, col+dc
                        
                        if r in range(Rows) and c in range(Cols) and (r,c) not in visit:
                            if grid[r][c] == 1:
                                return res
                            q.append((r,c))
                            visit.add((r,c))
                res+=1
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()
