class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        res =0;
        count =1;
        n =0
        for i in range(1,len(nums)):
            if nums[i] == nums[res]:
                count+=1
            else:
                count-=1
            if count == 0:
                res = i
                count =1
            print(count,res)
        
        for j in nums:
            if nums[res] == j:
                n +=1
        # print(n,res)
        if n > len(nums)//2:
            return nums[res]
        return -1
        
        