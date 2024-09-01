class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        def find_index(m):
            a, b = m,m
            while a >-1  and nums[a] == target:
                a -=1
            while b <len(nums) and nums[b] == target:
                b+=1
            return [a+1, b-1]
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return find_index(m)
            if nums[m] < target:
                l = m+1
            if nums[m]> target:
                r = m-1

        return [-1,-1]