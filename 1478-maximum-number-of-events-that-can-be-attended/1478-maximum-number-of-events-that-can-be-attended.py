class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        day = events[0][0]
        res = 0
        i = 0
        while heap or i<len(events):
            if not heap: day = events[i][0]
            while i<len(events) and events[i][0]==day:
                heapq.heappush(heap, events[i][1])
                i+=1
            
            if heap:
                heapq.heappop(heap)
                res+=1
            day+=1
            while heap and heap[0]<day:
                heapq.heappop(heap)
            
        # print(heap, day)
        return res