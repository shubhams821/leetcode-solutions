class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1.0 or n == 0: return 1.0
        if n < 0: 
            n = -n
            x = 1/x
        print(x,n)
        if (n%2): return x*(self.myPow(x*x, n//2))
        return self.myPow(x*x, n//2)