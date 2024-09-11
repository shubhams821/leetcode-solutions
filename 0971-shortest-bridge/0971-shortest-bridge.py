class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r,c):
            if r not in range(N) or c not in range(N) or (r,c) in visit or not grid[r][c]:
                return
            visit.add((r,c))
            for dr, dc in directions:
                dfs(dr+r, dc+c)
        
        def bfs():
            res, q = 0, deque(visit)
            while q:
                for i in range(len(q)):
                    row,col = q.popleft()
                    for dr, dc in directions:
                        r= row+ dr
                        c= col+ dc
                        if r not in range(N) or c not in range(N) or (r,c) in visit:
                            continue
                        print(grid[r][c])
                        if grid[r][c]:
                            print(0)
                            return res
                        q.append((r,c))
                        visit.add((r,c))
                res+=1
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r,c)
                    print(deque(visit))
                    return bfs()
