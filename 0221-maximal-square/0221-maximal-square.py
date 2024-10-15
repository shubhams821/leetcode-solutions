class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        Rows, Cols = len(matrix), len(matrix[0])
        res = [[0]*(Cols+1) for _ in range(Rows+1)]
        print(res)
        count = 0
        # res = [[0]*(Cols+1)]*(Rows+1)
        # print(res)
        for r in range(1,Rows+1):
            for c in range(1, Cols+1):
                if matrix[r-1][c-1]=="1":
                    res[r][c] = min(res[r-1][c], res[r][c-1], res[r-1][c-1]) + 1
                    count = max(count, res[r][c])
        return count**2