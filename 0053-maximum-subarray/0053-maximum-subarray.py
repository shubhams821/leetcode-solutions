class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msum = nums[0]
        res =0

        for i in nums:
            res+=i
            msum = max(res, msum)
            if res<0:
                res =0
           
            
            print(res)
        return msum