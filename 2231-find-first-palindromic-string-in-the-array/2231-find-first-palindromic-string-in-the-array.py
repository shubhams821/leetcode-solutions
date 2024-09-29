class Solution:
    def recur(self,s, l,r):
        if l>=r: return True
        if s[l]!= s[r]: return False
        return self.recur(s, l+1,r-1)
    def firstPalindrome(self, words: List[str]) -> str:
        for s in words:
            if self.recur(s,0,len(s)-1): return s
        return ""