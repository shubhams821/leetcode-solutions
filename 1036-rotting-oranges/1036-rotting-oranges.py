class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = [0]
        Rows, Cols = len(grid), len(grid[0])
        def bfs(q):
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    directions = [[1,0],[0,1],[-1,0],[0,-1]]
                    for dr, dc in directions:
                        r, c = row+dr, col+dc
                        if r in range(Rows) and c in range(Cols) and (r,c) not in visit and grid[r][c] == 1:
                            q.append((r,c))
                            visit.add((r,c))
                            grid[r][c] = 2     
                    # print(visit, q)
                if q:
                    time[0] +=1
                    print(q, time)
                # print("break")
        q = deque()
        visit = set()               
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))

        bfs(q)
        
        for r in range(Rows):
            if 1 in grid[r]:
                return -1
        return time[0]