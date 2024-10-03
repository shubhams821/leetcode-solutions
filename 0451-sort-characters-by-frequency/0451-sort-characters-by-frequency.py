class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for i in s:
            freq[i] = freq.get(i,0) +1
        res = []
        for k,v in freq.items():
            res.append([v,k])
        res = sorted(res, reverse = True)
        new = ""
        for v,k in res:
            new += k*v
        return new