class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ctoo = {']':'[',')':'(','}':'{'}

        for i in s:
            # print(stack)
            if i in ctoo:
                if stack and stack[-1]== ctoo[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        # print(stack)
        return True if not stack else False