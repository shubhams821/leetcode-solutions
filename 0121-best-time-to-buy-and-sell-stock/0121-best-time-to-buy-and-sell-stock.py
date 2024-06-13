class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i =0
        j=1

        mprof = 0
        while(j<len(prices)):
            prof = prices[j] - prices[i]

            if prof<0:
                i=j
            mprof = max(prof,mprof)
            j+=1
        return mprof