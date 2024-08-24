class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            print(nums[mid], l,r)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid-1
            if nums[mid] < target:
                l = mid+1
            print(nums[mid], l,r)
            
        return -1