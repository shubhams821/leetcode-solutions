class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) 
        if target%2: return False
        dp = set()
        dp.add(0)
        for val in nums:
            nextDp = set()
            for t in dp:
                nextDp.add(t+val)
                nextDp.add(t)
            dp = nextDp
        return True if target//2 in dp else False
