class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        resNums2 = [0]*(len(nums2))
        for i, num in enumerate(nums2):
            while stack and stack[-1][0] < num:
                tmp, tmp_idx = stack.pop()
                resNums2[tmp_idx] = num
            stack.append([num,i])
        while stack:
            tmp, tmp_idx = stack.pop()
            resNums2[tmp_idx] = -1
        print(resNums2)
        resNums1 = []
        for i in nums1:
            for idx,j in enumerate(nums2):
                if i ==j:
                    resNums1.append(resNums2[idx])
        return resNums1

# 5,5
# 1,4
# 2,3
# 4,2





        
        