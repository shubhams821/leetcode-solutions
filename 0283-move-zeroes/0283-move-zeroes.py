class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i =0
        for r in range(len(nums)):
            if nums[r]:
                nums[i], nums[r] = nums[r], nums[i]
                i+=1