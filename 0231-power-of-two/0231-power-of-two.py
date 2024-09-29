class Solution:
    def recur(self, a, n):
        if 2**a == n: return True
        if 2**a>n: return False
        return self.recur(a+1,n)

    def isPowerOfTwo(self, n: int) -> bool:
        return self.recur(0,n)