class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]

        heapq.heapify(stones)

        while(len(stones)>1):
            first = heappop(stones)
            second = heappop(stones)

            if first < second:
                heappush(stones, first-second)
        return -stones[0] if stones else 0 