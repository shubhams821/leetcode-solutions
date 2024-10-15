class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j =0,1
        mprof = 0
        while j <len(prices):
            prof = prices[j] - prices[i]
            mprof = max(prof, mprof)
            if prof < 0:
                i =j
            j+=1
        return mprof
            