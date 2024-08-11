class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visit = set()
        def dfs(i,j):
            if i <0 or j < 0 or i == Rows or j == Cols:
                return 0
            if grid[i][j] == 1 or (i,j) in visit:
                return 1
            
            visit.add((i,j))
            return min( dfs(i,j+1),
                        dfs(i+1, j),
                        dfs(i,j-1),
                        dfs(i-1,j))
        res = 0
        for i in range(Rows):
            for j in range(Cols):
                if not grid[i][j] and (i,j) not in visit:
                    res += dfs(i,j)
        return res