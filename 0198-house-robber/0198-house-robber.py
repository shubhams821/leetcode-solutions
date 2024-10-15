class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {-1:[0,0]}
        for i in range(len(nums)):
            dp[i] = [dp[i-1][1]+nums[i],max(dp[i-1])]
        return max(dp[len(nums)-1])