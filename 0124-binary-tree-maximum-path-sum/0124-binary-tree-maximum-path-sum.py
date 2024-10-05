# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [-float('inf')]

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left = max(0,left)
            right = max(0, right)
            res[0] = max(res[0], node.val + left + right)
            return max(left, right) + node.val
        dfs(root)
        return res[0]