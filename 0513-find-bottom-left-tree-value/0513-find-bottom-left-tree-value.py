# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res =  []
        q = collections.deque([root])
        while q:
            qLen = len(q)
            leftSide = None
            for i in range(qLen):
                node = q.popleft()
                if node:
                    leftSide = node
                    q.append(node.right)
                    q.append(node.left)
            if leftSide:
                res.append(leftSide.val)
        return res[-1]