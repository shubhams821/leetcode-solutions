class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visit = set()
        def dfs(r,c):
            if r not in range(Rows) or c not in range(Cols) or grid[r][c] == "0" or (r,c) in visit:
                return
            visit.add((r,c))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for dr,dc in directions:
                dfs(r+dr, c+dc)
        res = 0
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    res +=1
        return res