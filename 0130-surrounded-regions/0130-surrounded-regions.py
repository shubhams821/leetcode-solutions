class Solution:
    def solve(self, board: List[List[str]]) -> None:
        Rows, Cols = len(board), len(board[0])
        def dfs(i,j):
            if i not in range(Rows) or j not in range(Cols) or board[i][j] != "O":
                return
            board[i][j] = "T"
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i-1,j)
            return
        for r in range(Rows):
            for c in range(Cols):
                if r in [0, Rows-1] or c in [0, Cols-1]:
                    dfs(r,c)
        
        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] =="T":
                    board[r][c] = "O" 