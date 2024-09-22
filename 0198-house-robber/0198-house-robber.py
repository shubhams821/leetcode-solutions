class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        for i in range(len(nums)):
            dp[i] = max(dp.get(i-2,0)+nums[i], dp.get(i-1,0))
        print(dp)
        return dp[i]