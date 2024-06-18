class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums1 = [-int(i) for i in nums]

        heapq.heapify(nums1)
        res = -2147483649

        print(nums1)
        i=0
        while(k>0 and i<len(nums)):
            temp = heapq.heappop(nums1)
            print(temp,res,k)
            if True:
                res = temp
                k-=1
            
            i+=1

        return str(-temp)
