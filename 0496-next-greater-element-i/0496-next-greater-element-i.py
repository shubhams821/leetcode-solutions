class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        resNums2 = {}
        for i, num in enumerate(nums2):
            while stack and stack[-1][0] < num:
                tmp, tmp_idx = stack.pop()
                resNums2[tmp] = num
            stack.append([num,i])
        while stack:
            tmp, tmp_idx = stack.pop()
            resNums2[tmp] = -1
        # print(resNums2)
        # return []
        return [resNums2[i] for i in nums1]

# 5,5
# 1,4
# 2,3
# 4,2





        
        