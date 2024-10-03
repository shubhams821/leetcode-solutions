class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+ 1
        
        freq_lst = []
        for k1,v in freq.items():
            heapq.heappush(freq_lst, (-v,k1))
        print(freq_lst)
        res = []
        for i in range(k):
            v,k1 = heapq.heappop(freq_lst)
            res.append(k1)
        return res