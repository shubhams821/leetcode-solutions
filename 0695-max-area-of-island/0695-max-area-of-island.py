class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visit = set()
        def dfs(i,j):
            if i not in range(Rows) or j not in range(Cols) or not grid[i][j] or (i,j) in visit:
                return 0
            visit.add((i,j))
            return (1 + dfs(i+1,j)+
                        dfs(i,j+1)+
                        dfs(i-1,j)+
                        dfs(i,j-1))
        res =0
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] not in visit:
                    tmp = dfs(r,c)
                    res = max(res, tmp)

        return res