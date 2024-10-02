class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        Row, Col = len(grid), len(grid[0])
        res = [[float('inf')]*(Col+1)]*(Row+1)
        res[Row][Col-1] = 0
        for r in range(Row-1,-1,-1):
            for c in range(Col-1,-1,-1):
                res[r][c] = min(res[r+1][c], res[r][c+1]) + grid[r][c]
        return res[0][0]
