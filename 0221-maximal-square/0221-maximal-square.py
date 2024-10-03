class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        Rows, Cols = len(matrix), len(matrix[0])
        grid = [[0]*(Cols+1) for _ in range(Rows+1)]
        print(grid)
        res =0
        for r in range(1,Rows+1):
            for c in range(1, Cols+1):
                if matrix[r-1][c-1] == "1":
                    grid[r][c] = min(grid[r-1][c], grid[r][c-1], grid[r-1][c-1]) +1
                res = max(res, grid[r][c])
        print(grid)
        return res**2