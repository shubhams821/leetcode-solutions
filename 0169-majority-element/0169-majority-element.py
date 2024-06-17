class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count =1
        res = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[res]:
                count+=1
            else:
                count-=1

            if count ==0:
                count =1
                res =i
        return nums[res]