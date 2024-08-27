class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Rows, Cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c, visit, prevHeight):
            if ((r,c) in visit or
                r not in range(Rows) or
                c not in range(Cols) or 
                heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            dfs(r+1,c, visit, heights[r][c])
            dfs(r,c+1, visit, heights[r][c])
            dfs(r-1,c, visit, heights[r][c])
            dfs(r,c-1, visit, heights[r][c])
        
        for c in range(Cols):
            dfs(0,c, pac, heights[0][c])
            dfs(Rows-1, c, atl, heights[Rows-1][c])
        for r in range(Rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r, Cols-1, atl, heights[r][Cols-1])
        res =[]
        for r in range(Rows):
            for c in range(Cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res