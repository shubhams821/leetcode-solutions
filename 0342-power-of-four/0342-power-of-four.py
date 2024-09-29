class Solution:
    # def recur(self, a, n):
    #     if 
    def isPowerOfFour(self, n: int) -> bool:
        if n==1: return True
        for i in range(0,32,2):
            tmp = 4<<i
            if tmp ==n: return True
            if tmp >n: return False
        return False