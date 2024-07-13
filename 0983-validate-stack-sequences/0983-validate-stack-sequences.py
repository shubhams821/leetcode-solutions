class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        k=0
        for i in range(len(pushed)):
            stack.append(i)
            print(stack)
            while stack and pushed[stack[-1]] == popped[k]:
                k+=1
                stack.pop()
        while stack and pushed[stack[-1]] == popped[k]:
                k+=1
                stack.pop()
        print(stack)
                
        return False if stack else True


