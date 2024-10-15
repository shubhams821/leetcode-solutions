class Solution:
    def minimumSteps(self, s: str) -> int:
        l =0
        res =0
        s = list(s)
        for r in range(len(s)):
            if s[r] == "0":
                s[l],s[r]=s[r],s[l]
                res+=(r-l)
                l +=1
                
        print(s)
        return res
