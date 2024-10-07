class Solution:
    import re
    def check_int(self,value):
        # This regex matches optional leading '+' or '-' followed by digits
        pattern = r'^[+-]?\d+$'
        return bool(re.match(pattern, value))

    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        def recur(s):
            if len(s) <= 2: 
                # print(s)
                return [int(s)]
            res = []
            for i in range(len(s)):
                if not self.check_int(s[i]):
                    # print(s[i])
                    # print(s[:i],s[i+1:])
                    ans_l = recur(s[:i])
                    ans_r = recur(s[i+1:])
                    
                    # print(ans_r, s[i+1:])
                    for x in ans_r:
                        for y in ans_l:
                            if s[i] == "*":
                                res.append(x*y)
                            elif s[i] == "+":
                                res.append(x+y)
                            else:
                                res.append(y-x)
            return res   

        return recur(expression)