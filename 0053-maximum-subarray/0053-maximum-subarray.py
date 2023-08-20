class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum =nums[0]
        res =0
        for i in nums:
            if res <0:
                res =0
            res+=i
            maxsum = max(maxsum,res)
        return maxsum
        

    