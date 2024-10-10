class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        temp = []
        mx = 0
        for i in nums[::-1]:
            mx = max(i,mx)
            temp.append(mx)
        temp = temp[::-1]
        print(temp)
        i,j = 0, 0
        res =0
        while i<len(nums) and j< len(nums):
            if nums[i] <= temp[j]:
                res = max(res, j-i)
            else:
                i+=1
            j+=1
        return res
