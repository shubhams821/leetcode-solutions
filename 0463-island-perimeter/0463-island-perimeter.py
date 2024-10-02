class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visit = set()
        def dfs(r,c):
            if r not in range(Rows) or c not in range(Cols) or not grid[r][c] :
                return 1
            if (r,c) in visit:
                return 0
            visit.add((r,c))
            return dfs(r,c+1) + dfs(r+1,c) +dfs(r,c-1) + dfs(r-1,c)
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c]:
                    return dfs(r,c) 