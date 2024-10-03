class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        freq = [(-v,k1) for k1,v in counter.items()]
        heapify(freq)
        res =  []
        while k>0:
            v,k1 = heapq.heappop(freq)
            res.append(k1)
            k-=1
        return res
