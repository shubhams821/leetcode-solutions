class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {i:[] for i in range(1,n+1)}
        for s, d, w in times:
            edges[s].append([d,w])
        print(edges)
        
        visit = set()
        minHeap = [(0,k)]
        t = 0
        while minHeap:
            w1, v1 = heapq.heappop(minHeap)
            if v1 in visit:
                continue
            visit.add(v1)
            t = max(t, w1)
            print(edges[v1])
            for v2, w2 in edges[v1]:
                if v2 not in visit:
                    heapq.heappush(minHeap,(w1+w2, v2))
            # print(minHeap)

        return t if len(visit) == n else -1