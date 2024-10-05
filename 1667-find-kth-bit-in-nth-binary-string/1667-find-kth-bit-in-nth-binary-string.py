class Solution:
    def rev_inv(self, s):
        s1 = ""
        for i in s:
            if i == "0":
                s1+= "1"
            else:
                s1+= "0"
        return s1[::-1]
    def findKthBit(self, n: int, k: int) -> str:
        res = '0'
        while n>0:
            res = res + "1" + self.rev_inv(res)
            n-=1
        return res[k-1]