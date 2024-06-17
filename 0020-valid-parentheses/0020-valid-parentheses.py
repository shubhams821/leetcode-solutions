class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ctoo = {')':'(','}':'{',']':'['}

        for i in s:
            if i in ctoo:
                if stack and ctoo[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False