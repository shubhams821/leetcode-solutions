class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        visit = set()
        time = [0]
        def bfs(q):
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    directions = [[1,0],[0,1],[-1,0],[0,-1]]
                    for dr, dc in directions:
                        r, c = dr+row, dc+col
                        if r in range(Rows) and c in range(Cols) and grid[r][c] == 1 and (r,c) not in visit:
                            grid[r][c] = 2
                            q.append((r,c))
                            visit.add((r,c))
                if q:
                    time[0]+= 1
        q = deque()
        for r in range(Rows):
             for c in range(Cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
        bfs(q)
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    return -1
        return time[0]
