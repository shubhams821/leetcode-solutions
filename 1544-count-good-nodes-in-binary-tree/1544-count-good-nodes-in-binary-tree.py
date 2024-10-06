# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def dfs(node, maxVal):
            if not node:
                return 
            count = 1 if node.val >= maxVal else 0
            res[0] += count
            maxVal = max(maxVal, node.val)
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        dfs(root, root.val)
        return res[0]
