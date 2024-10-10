class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBits(res):
            count = 0
            for i in range(20):
                if res & 1<<i: count+=1
            return count
        dp =[0]*(n+1)
        for i in range(n+1):
            dp[i] = countBits(i)
        return dp