class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(len(graph))}
        for i, lst in enumerate(graph):
            adj[i].extend(lst)
        # print(adj)
        visit, cycle = set(), set()
        output = []
        def dfs(node):
            if node in cycle: return False
            if node in visit: return True
            cycle.add(node)
            for nei in adj[node]:
                if not dfs(nei): return False
            cycle.remove(node)
            visit.add(node)
            # print(node)
            output.append(node)
            return True
        for i in adj:
            dfs(i)
        return sorted(output)