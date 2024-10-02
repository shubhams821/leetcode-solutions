class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visit = set()
        def dfs(r,c):
            if r not in range(Rows) or c not in range(Cols):
                return 0
            if grid[r][c] or (r,c) in visit:
                return 1
            visit.add((r,c))
            return min(dfs(r+1,c), dfs(r,c+1), dfs(r-1,c), dfs(r,c-1))
        res = 0
        for r in range(Rows):
            for c in range(Cols):
                if not grid[r][c] and (r,c) not in visit:
                    res+= dfs(r,c)
        return res