class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        for i in range(1,n+1):
            if target[-1] < i:
                break
            if i in target:
                stack.append('Push')
            else:
                stack.append('Push')
                stack.append('Pop')

        return stack