class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        freq = [(-v,k) for k,v in counter.items()]
        heapify(freq)
        new = ""
        while freq:
            v1, k1 = heapq.heappop(freq)
            new += k1*(-v1)
        return new