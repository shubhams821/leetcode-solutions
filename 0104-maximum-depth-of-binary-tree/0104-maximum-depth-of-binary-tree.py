# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])
        level = -1

        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
            level+=1
        return level
