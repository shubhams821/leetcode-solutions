class Solution:
    def maximum69Number (self, num: int) -> int:
        stri = str(num)
        new=''
        isit = False
        for i in range(len(stri)):
            if stri[i] == '6' and isit == False:
                new+='9'
                isit = True
            else:
                new += stri[i]
        print(new)
        return int(new)
                