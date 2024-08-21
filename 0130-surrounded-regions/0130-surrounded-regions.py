class Solution:
    def solve(self, board: List[List[str]]) -> None:
        Rows, Cols = len(board), len(board[0])
        def dfs(i,j):
            print(i,j)
            if (i <0 or i == Rows or j <0 or j == Cols or board[i][j] != "O"):
                return 
            board[r][c] = "T"
            dfs(i+1,j)
            dfs(i-1,j)
            return
            dfs(i,j+1)
            dfs(i,j-1)
        for r in range(Rows):
            for c in range(Cols):
                if (board[r][c] == "O" and 
                    (r in [0, Rows-1] or c in [0,Cols-1])):
                    print(r,c)
                    # break
                    dfs(r,c)
                    
                

        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] == "T":
                    board[r][c] = "O"