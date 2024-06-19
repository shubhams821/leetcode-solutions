class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        msum = nums[0]

        for i in nums:
            res +=i
            msum = max(msum,res)
            if res <0:
                res =0
        return msum