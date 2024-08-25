class Solution:
    def binaryGap(self, n: int) -> int:
        lst = []
        while n:
            lst.append(n%2)
            n//=2
        lst = lst[::-1]
        i = 0
        while lst[i] != 1:
            i+=1
        res =0
        print(lst)
        for r in range(i,len(lst)):
            print(i,r)
            if lst[r]==1:
                res = max(res, r-i)
                i = r
        return res  if sum(lst)>1 else 0