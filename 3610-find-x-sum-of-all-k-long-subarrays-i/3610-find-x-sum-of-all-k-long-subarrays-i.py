class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []

        for i in range(0, len(nums)-k+1):
            count = Counter(nums[i:i+k])
            res1 = [(-v,-k) for k,v in count.items()]
            heapify(res1)
            count_elem = 0
            for j in range(x):
                if res1:
                    v1, k1 = heapq.heappop(res1)
                    count_elem += k1*v1
            res.append(count_elem)
        return res
            