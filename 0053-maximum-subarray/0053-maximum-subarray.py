class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msum = nums[0]
        res =0

        for i in nums:
            if res <0:
                res =0
            res +=i

            msum = max(res,msum)
        return msum