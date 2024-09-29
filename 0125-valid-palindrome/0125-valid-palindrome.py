class Solution:
    def recur(self,s, l,r):
        if l>=r: return True
        if s[l] != s[r]: return False
        return self.recur(s, l+1,r-1)
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^A-Za-z0-9]+', '', s)
        l,r = 0, len(s)-1
        print(s)
        return self.recur(s.lower(), l,r)