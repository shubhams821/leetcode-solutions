class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        # list = [s[i:i+10] for i in range(len(s)-10+1)]
        res1 =set()
        res2 = set()
        for i in range(len(s)-10+1):
            j = s[i:i+10]
            if j not in res1:
                res1.add(j)
            else:
                res2.add(j)
        return res2