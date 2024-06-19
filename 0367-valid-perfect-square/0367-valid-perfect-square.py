class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num

        while(l<=r):
            m = (l+r)//2
            if m**2 == num:
                return m
            elif m**2> num:
                
                r = m-1
            else:
                l =m+1
        