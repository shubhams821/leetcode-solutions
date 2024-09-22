class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        for i in range(n):
            num = i+1
            tmp = []
            while num:
                tmp.append(num%10)
                num //=10
            res.append([tmp[::-1], i+1])
        # print(sorted(res))
        return [i for _,i in sorted(res)]