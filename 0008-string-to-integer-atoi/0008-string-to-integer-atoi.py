class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(' ')
        print(s)
        lst =[]
        num = '0123456789'
        for i in s:
            if i == " ":
                if lst == []:
                    continue
                else:
                    break
            if (i == '-'or i == '+') and lst ==[]: 
                lst.append(i)
            elif i in num:
                lst.append(i)
            else:
                break
        # p = int('4')
        # print(p)
        s = ''.join(lst)
        print(s)
        if s == '' or s == '-' or s == '+':
            return 0
        # return 0
        else:
            res = int(s)
            if int(res) < -(2**31):
                return -(2**31)
            elif int(res) > (2**31 - 1):
                return (2**31 - 1)
            else:
                return int(res)
        # print(s)
        