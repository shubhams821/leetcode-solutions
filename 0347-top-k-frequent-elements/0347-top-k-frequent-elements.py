class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+ 1
        freq_lst = [(-v,k) for k,v in freq.items()]
        heapify(freq_lst)
        res = []
        for i in range(k):
            v,k = heapq.heappop(freq_lst)
            res.append(k)
        return res