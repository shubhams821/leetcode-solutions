class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visit = set()

        def dfs(i,j):
            if i not in range(Rows) or j not in range(Cols):
                return 0
            if (i,j) in visit or grid[i][j]:
                return 1
            visit.add((i,j))
            return min(dfs(i+1,j),
                        dfs(i,j+1),
                        dfs(i-1,j),
                        dfs(i,j-1))
        res =0
        for r in range(Rows):
            for c in range(Cols):
                if not grid[r][c] and (r,c) not in visit:
                    res +=dfs(r,c)
                    
        return res