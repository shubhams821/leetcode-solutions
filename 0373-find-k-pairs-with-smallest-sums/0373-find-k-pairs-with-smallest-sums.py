class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        a,b = 0,0
        for i in nums1:
            heapq.heappush(minHeap,(i+nums2[0],0))
        print(minHeap)
        while k>0:
            s, pos = heapq.heappop(minHeap)
            res.append([s -nums2[pos], nums2[pos]])
            k-=1
            if pos < len(nums2)-1: 
                heapq.heappush(minHeap, (s - nums2[pos]+nums2[pos+1], pos+1))
        return res

