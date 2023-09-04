class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        prof =0
        for i in range(1,len(prices)):
            sell = prices[i]
            if buy< sell:
                prof = max(prof, sell - buy)
            else:
                buy = sell
        return prof
