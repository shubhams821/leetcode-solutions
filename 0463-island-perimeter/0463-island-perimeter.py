class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # if not grid:
        #     return 0
        Rows, Cols = len(grid), len(grid[0])
        visit = set()

        def dfs(i,j):
            if i not in range(Rows) or j not in range(Cols) or not grid[i][j]:
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            perim = dfs(i,j+1)
            perim += dfs(i+1,j)
            perim += dfs(i,j-1)
            perim += dfs(i-1,j)
            return perim
        res = 0
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] and (r,c) not in visit:
                    res += dfs(r,c)
        return res