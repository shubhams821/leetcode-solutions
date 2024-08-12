class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        def dfs(i,j):
            if i not in range(rows) or j not in range(cols) or grid[i][j] ==0:
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            perim = dfs(i,j+1)
            perim += dfs(i+1, j)
            perim += dfs(i, j-1)
            perim += dfs(i-1,j)
            return perim
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)