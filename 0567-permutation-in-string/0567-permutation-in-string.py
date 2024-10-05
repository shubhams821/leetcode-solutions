class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = Counter(s1)
        for i in range(0,len(s2)-len(s1)+1):
            newS2 = s2[i:i+len(s1)]
            counterNewS2 = Counter(newS2)
            if countS1 == counterNewS2:
                return True
        return False