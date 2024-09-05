class Solution:
    def solve(self, board: List[List[str]]) -> None:
        Rows, Cols = len(board), len(board[0])
        visit = set()

        def bfs(i,j):
            q = collections.deque()
            q.append([i,j])
            visit.add((i,j))
            board[i][j] = "T" 
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    directions = [[1,0],[0,1],[-1,0],[0,-1]]
                    for dr, dc in directions:
                        r,c = row+dr, col+dc
                        if r in range(Rows) and c in range(Cols) and board[r][c] == "O" and (r,c) not in visit:
                            q.append([r,c])
                            visit.add((r,c))
                            board[r][c] = "T" 
                            print(r,c)
        for r in range(Rows):
            for c in range(Cols):
                if r in [0,Rows-1] or c in [0,Cols-1]:
                    if (r,c) not in visit and board[r][c] == "O":
                        bfs(r,c)
                        print(r,c)
        print(board)
        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"