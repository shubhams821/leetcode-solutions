class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [ -int(i) for i in nums]
        heapq.heapify(nums)
        while k>0:
            res = heapq.heappop(nums)
            k-=1
        return str(-res)
