class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        track = False
        for i in s:
            while stack and (stack[-1] + i == "AB" or stack[-1] + i == "CD"):
                print(stack)
                stack.pop()
                track = True
                break
            if not track:
                stack.append(i)
            track = False
        print(stack)
        return len(stack)