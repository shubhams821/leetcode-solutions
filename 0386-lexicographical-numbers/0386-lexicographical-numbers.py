class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(curr):
            if curr >n:
                return
            res.append(curr)
            # curr *= 10
            for i in range(10):
                dfs(curr*10 +i)
        for i in range(9):
            dfs(i+1)
        return res