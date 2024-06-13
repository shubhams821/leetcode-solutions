class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res =0
        count =1

        for i in range(1, len(nums)):
            if nums[res]== nums[i]:
                count+=1
            else:
                count -=1
            if count ==0:
                count =1
                res =i
        return nums[res]