class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}

        for i in range(N):
            for j in range(i+1, N):
                [x1, y1], [x2, y2] = points[i], points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([j,dist])
                adj[j].append([i,dist])
        
        #prims
        res = 0
        visit = set()
        minHeap = [[0,0]]
        while len(visit)< N:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            res+=cost
            visit.add(i)
            for nei, neiCost in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])
        # print(adj)
        return res