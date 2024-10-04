class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recur(temp, idx):
            if idx== len(nums):
                res.append(temp)
                return 
            recur(temp, idx+1)
            recur(temp+[nums[idx]], idx+1)
        recur([],0)
        return res
            