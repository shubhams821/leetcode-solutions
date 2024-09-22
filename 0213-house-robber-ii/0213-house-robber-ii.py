class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        dp1 = {}
        dp2 = {}
        for i in range(len(nums)-1):
            dp1[i] = max(dp1.get(i-1,0), dp1.get(i-2,0)+nums[i])
            dp2[i+1] = max(dp2.get(i,0), dp2.get(i-1,0)+nums[i+1])
        print(dp1, dp2)
        return max(dp1.get(len(nums)-2,0), dp2.get(len(nums)-1,0))
        