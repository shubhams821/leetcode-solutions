class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0]*(n) for _ in range(m)]
        res[0][0] = 1
        
        for r in range(m):
            for c in range(n):
                direc = [[-1,0],[0,-1]]
                for dr, dc in direc:
                    if r+dr in range(m) and c+dc in range(n):
                        res[r][c] += res[r+dr][c+dc]
        print(res)
        return res[m-1][n-1]