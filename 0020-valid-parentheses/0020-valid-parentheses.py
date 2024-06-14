class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        ctoo = {')':'(',']':'[',"}":'{'}
        for i in s:
            if i in ctoo:
                if stack and stack[-1]== ctoo[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
        stack =[]
        ctoo = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in ctoo:
                if stack and stack[-1]==ctoo[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False