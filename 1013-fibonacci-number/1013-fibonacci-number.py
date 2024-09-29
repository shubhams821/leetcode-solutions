class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        for i in range(n-1):
            tmp = a
            a = b
            b = tmp+ a
        return b if n else 0