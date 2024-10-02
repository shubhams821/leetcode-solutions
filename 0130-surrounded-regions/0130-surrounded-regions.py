class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        Rows, Cols = len(board), len(board[0])
        visit = set()
        def dfs(r,c):
            if r not in range(Rows) or c not in range(Cols) or board[r][c] =="X" or (r,c) in visit:
                return
            visit.add((r,c))
            board[r][c] = "T"
            dfs(r,c+1)
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
        
        for r in range(Rows):
            for c in range(Cols):
                if (r in [0,Rows-1] or c in [0,Cols-1]) and board[r][c]== "O":
                    dfs(r,c)

        
        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"

