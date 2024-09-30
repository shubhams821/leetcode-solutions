class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res, stack = [0]*(len(prices)), []
        for idx,price in enumerate(prices):
            while stack and stack[-1][0] >= price:
                tmp_price, tmp = stack.pop()
                res[tmp] = tmp_price-price
            stack.append([price, idx])
        while stack:
            tmp_price, tmp = stack.pop()
            res[tmp] = tmp_price
        return res


# 3
# 2

# [8-4,4-2, 6-2, 2, 3]