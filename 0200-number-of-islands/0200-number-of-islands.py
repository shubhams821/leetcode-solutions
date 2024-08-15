class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visit = set()
        def dfs(i,j):
            if i not in range(Rows) or j not in range(Cols) or (i,j) in visit or grid[i][j] == "0":
                return
            visit.add((i,j))
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i-1,j)
            return
        island =0
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    island +=1
        return island
