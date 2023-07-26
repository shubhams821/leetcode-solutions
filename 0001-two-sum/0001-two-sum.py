class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l1 = nums
        for i in range(len(l1)):
            for j in range(len(l1)):
                if i<j:
                    # print([i,j])
                    if l1[i]+l1[j]==target:
                        print([i,j])
                        return [i,j]