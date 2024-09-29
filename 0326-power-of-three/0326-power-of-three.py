class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def recur(a,n):
            if 3**a == n: return True
            if 3**a >n: return False
            return recur(a+1,n)
        return recur(0, n)