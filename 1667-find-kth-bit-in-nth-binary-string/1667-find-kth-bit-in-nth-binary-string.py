class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        res = "0"
        for i in range(n-1):
            res = res + "1" + res[::-1].replace("1", "a").replace("0", "1").replace("a","0")
        return res[k-1]