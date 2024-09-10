class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = {i: nodes for i, nodes in enumerate(graph)}
        cycle, safe  = set(), set()

        def dfs(node):
            if node in cycle: 
                return False
            if node in safe:
                return True
            cycle.add(node)
            for nei in adj[node]:
                if not dfs(nei): return False
            cycle.remove(node)
            safe.add(node)
            return True
        output = []
        for node in range(len(graph)):
            if node not in cycle:
                if dfs(node):
                    output.append(node)
        return output